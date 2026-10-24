"""Bounded subprocess execution and optional sequential PDF previews."""
import os
from pathlib import Path
import signal
import subprocess


def run(args: list[str], timeout: int = 60) -> str:
    """Run without a shell; reap the process and kill any remaining children."""
    environment = dict(os.environ, LC_ALL="C", LANG="C")
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               start_new_session=True, env=environment)
    try:
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired as error:
            raise RuntimeError(f"{Path(args[0]).name} timed out after {timeout}s") from error
    finally:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.communicate()
    if process.returncode:
        detail = stderr.decode("utf-8", errors="replace")[-2000:]
        raise RuntimeError(f"{Path(args[0]).name} failed ({process.returncode}): {detail}")
    return stdout.decode("utf-8", errors="replace")


def make_previews(pdf: Path, pages: int, executable: str | None) -> dict:
    if not executable:
        return {"status": "unavailable", "reason": "Optional pdftoppm not found", "files": []}
    files = []
    for page in range(1, pages + 1):
        prefix = pdf.parent / f"{pdf.stem}-page-{page}"
        target = prefix.with_suffix(".png")
        if target.exists():
            raise ValueError(f"Refusing existing preview: {target.name}")
        run([executable, "-f", str(page), "-l", str(page), "-singlefile",
             "-r", "96", "-png", str(pdf), str(prefix)])
        if not target.is_file() or target.stat().st_size == 0:
            raise RuntimeError(f"pdftoppm did not create {target.name}")
        files.append(target.name)
    return {"status": "created", "dpi": 96, "files": files}
