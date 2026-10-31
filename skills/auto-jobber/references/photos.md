# Optional applicant portraits

The applicant and agent decide whether a CV uses a photograph. Use only a supplied or authorized image. If a profile site blocks public retrieval, ask for an upload or accessible image link; do not substitute a different person's picture or bypass access controls. Do not infer personality or qualifications from appearance.

Store the original and any useful CV crop in the applicant's chosen project folders. Keep the original unchanged when producing a head-and-shoulders crop. Check framing, resolution and unwanted metadata. The photo is a presentation asset, not a duplicated career record.

## Native HTML/CSS helpers

JPEG and static PNG portraits are supported. Use a relative `img src` in the editable HTML and pass the explicitly authorized asset root when previewing or sealing. For example, a CV under `cv/` can use `../profile/photo-cv.jpg` with the repository root authorized:

```html
<img class="portrait" src="../profile/photo-cv.jpg" alt="Applicant portrait">
```

```bash
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" preview \
  --language en --html "$PROJECT/cv/cv.en.html" \
  --css "$PROJECT/template/cv.css" --asset-root "$PROJECT"
# After actual approval, use the same source options with seal.
```

A relative stylesheet link may point to the exact file selected by `--css`; snapshots normalize it to `cv.css`. The legacy `cv.css` link remains supported. Other stylesheet resources and CSS imports remain forbidden.

Remote image URLs, authored data URLs, absolute image paths, SVG, unsupported formats, symlinks, paths outside the authorized root, active attributes and `srcset` are rejected. Raster inputs are bounded to 5 MiB, 8192 pixels per side and 20 million pixels, then decoded with Pillow; malformed or animated images are rejected. Successful decoding does not prove image quality or identity: inspect the rendered portrait as well.

Pillow is required only for native portrait validation. If it is missing, the helper reports that requirement rather than accepting an unvalidated image; photo-free documents remain supported. Install it in the chosen Python environment when portraits are wanted, for example `python3 -m pip install Pillow`. Do not disable image checks to avoid the dependency.

Generated standalone HTML embeds the authorized raster bytes; it does not depend on the original image location or load a remote portrait. Content Security Policy permits generated image data only when images exist; other external-resource restrictions remain unchanged.

## Retain the reviewed image

Sealed baselines retain referenced raster files under `portrait-assets/` with digests and original-source metadata. Changing or removing the master portrait requires reviewing and resealing the affected language variant before a new application is captured.

Existing applications use their frozen input assets, not a later live photograph. Builds and archives retain and hash those assets. Missing or changed snapshots fail verification. Do not modify a finished build to swap its picture or represent its old verification as valid.

Before approval, inspect every relevant page for image visibility, crop, aspect ratio, contrast, layout balance and text readability. A photograph on the CV does not imply that it belongs on the cover letter. Rendering success, integrity checks and visual inspection are separate from applicant approval.
