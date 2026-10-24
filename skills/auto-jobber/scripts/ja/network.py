"""Small HTTPS fetcher with per-hop public-address checks and pinned connections."""
import http.client
import ipaddress
import socket
import ssl
from urllib.parse import urljoin, urlsplit

from .web_text import readable_text

LIMIT = 2 * 1024 * 1024


class _PinnedHTTPS(http.client.HTTPSConnection):
    def __init__(self, hostname, address, port):
        super().__init__(hostname, port, timeout=15, context=ssl.create_default_context())
        self.address = address

    def connect(self):
        raw = socket.create_connection((self.address, self.port), self.timeout)
        try:
            self.sock = self._context.wrap_socket(raw, server_hostname=self.host)
        except BaseException:
            raw.close()
            raise


def _destination(url):
    parts = urlsplit(url)
    if parts.scheme != "https" or not parts.hostname or parts.username is not None:
        raise ValueError("Only credential-free HTTPS URLs are allowed")
    if parts.password is not None or any(ord(c) < 33 for c in url):
        raise ValueError("Invalid URL characters or credentials")
    host = parts.hostname.encode("idna").decode("ascii")
    if host.rstrip(".").lower() == "localhost":
        raise ValueError("Localhost is not allowed")
    port = parts.port or 443
    addresses = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    ips = {entry[4][0] for entry in addresses}
    if not ips:
        raise ValueError("Hostname has no addresses")
    for address in ips:
        ip = ipaddress.ip_address(address)
        if not ip.is_global or ip.is_multicast or ip.is_reserved or ip.is_unspecified:
            raise ValueError("Hostname resolves to a nonpublic address")
    return parts, host, port, sorted(ips)[0]


def fetch_text(url: str) -> str:
    """Fetch at most 2 MiB; validate and pin an address on every redirect hop.

    Socket operations time out after 15 seconds; DNS uses the system resolver.
    This is not a wall-clock deadline or a substitute for network isolation.
    """
    for hop in range(4):
        parts, host, port, address = _destination(url)
        connection = _PinnedHTTPS(host, address, port)
        try:
            target = parts.path or "/"
            if parts.query:
                target += "?" + parts.query
            connection.request("GET", target, headers={"Accept": "text/html, text/plain",
                                                       "Accept-Encoding": "identity"})
            response = connection.getresponse()
            if response.status in (301, 302, 303, 307, 308):
                location = response.getheader("Location")
                if not location or hop == 3:
                    raise ValueError("Missing redirect target or redirect limit exceeded")
                url = urljoin(url, location)
                continue
            if response.status != 200:
                raise ValueError(f"HTTP status {response.status}")
            content_type = response.headers.get_content_type()
            if content_type not in ("text/html", "text/plain"):
                raise ValueError("Response must be HTML or plain text")
            if response.getheader("Content-Encoding", "identity").lower() != "identity":
                raise ValueError("Compressed responses are not accepted")
            length = response.getheader("Content-Length")
            if length is not None and (int(length) < 0 or int(length) > LIMIT):
                raise ValueError("Response exceeds size limit")
            body = response.read(LIMIT + 1)
            if len(body) > LIMIT:
                raise ValueError("Response exceeds size limit")
            charset = response.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return readable_text(text) if content_type == "text/html" else text
        finally:
            connection.close()
    raise ValueError("Redirect limit exceeded")
