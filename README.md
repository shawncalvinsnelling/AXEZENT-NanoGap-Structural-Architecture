# AXEZENT NanoGap Structural Architecture

**Research and design: Shawn Calvin Snelling** · Original cube v1.0 (July 2026) · Website release prepared November 11, 2026.

This repository is a **GitHub Pages-ready research website** for the AXEZENT graded gyroid cube, original mathematical generator, selected STL geometry, an original cube CAD render and a photograph of a physical sample shared by the author. The site includes a browser-only mathematical field explorer and explicit validation boundaries.

> **Status:** Geometric model documented; experimental material performance and comparative superiority unverified. The photographed physical sample is not yet linked to complete print/process metadata. A proposed NanoGap wall is not included as a fabricated, validated product.

## Quick start

The repository is already published at `https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture`. After cloning or downloading the repository, run `python scripts/reassemble_assets.py` to reconstruct the original printed-cube photograph and calibration STL, verifying their SHA-256 values. Open `index.html` or run `python -m http.server 8000` for a local preview.

## GitHub Pages — deployed via Actions

GitHub Actions completed the build **and Pages deployment** successfully on November 11, 2026 (US Central time). The repository is already created and uploaded; no re-upload is required. The [Publish AXEZENT research website](https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture/actions/workflows/pages.yml) workflow reconstructs source assets, verifies hashes, runs the tests, and deploys automatically after pushes to `main`.

1. Open [Settings → Pages](https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture/settings/pages) and keep **Build and deployment → Source = GitHub Actions**.
2. Use **Visit site** there to confirm the public address and visually inspect galleries, downloads and mathematical controls.
3. If a future workflow fails, inspect its Actions logs and rerun after fixing the cause.

The site address reported by GitHub Pages should be `https://shawncalvinsnelling.github.io/AXEZENT-NanoGap-Structural-Architecture/`. A successful deployment is confirmed in Actions; a separate browser visual check is recommended.

### Local reproduction and validation

```powershell
python scripts/reassemble_assets.py
python -m unittest discover -s tests -v
python -m http.server 8000
```

The mathematics and an independent regression suite are described in [NanoGap mathematical verification](docs/NANOGAP_MATHEMATICAL_AUDIT.md). The site runs on static HTML, CSS, browser JavaScript and GitHub Actions; no additional hosting provider is required.

## Structure

- `index.html` — complete research website
- `assets/images/` — CAD render, actual physical sample photograph and explanatory diagram
- `assets/models/` — original outer-frame STL; exact calibration STL rebuilt from the verified parts
- `source/` — original Python generator and historical design manifest
- `docs/` — validation record, laboratory study protocol, provenance and research rights
- `assets/documents/` — technical PDF supplied in the MIT research correspondence
- `tests/` — automated static page and artifact checks

The master 63.5 mm high-resolution file is 84.8 MB, unsuitable for GitHub's browser uploader. It was provided directly to the MIT/Northeastern corresponding authors. Do not call the calibration or outer-frame STL the full master model.

## Citation and references

See `CITATION.cff` and https://doi.org/10.1038/s41586-026-11191-2 for the separately published 2026 MIT/Northeastern study. This site does not claim endorsement or collaboration by those institutions.

## Public release / copyright

Read `docs/RIGHTS_AND_USE.md`: this repository is already public and discloses the generator, equations, and selected model files. That can affect patent or trade-secret strategies; all-rights-reserved language does not undo the disclosure. No open-source license is implied by default.

### Maintenance

The repository is already populated. Use ordinary Git commits or the GitHub web editor for future changes. Preserve all original v1.0 design files and the documented limitations when adding new proposed variants.


## Binary asset fidelity and automated publishing

The full-size **original 38.1 mm calibration STL** and **full-resolution printed-cube photograph** are preserved *losslessly* as chunks in `data/asset-parts/` to make the initial GitHub transfer reliable. This is not a change to the original geometry. `scripts/reassemble_assets.py` combines the chunks, verifies their original SHA-256 hashes, and writes the exact files to the documented asset paths. The Actions build runs this step before validation and deployment. Run the same script locally after cloning to obtain all original research-site assets.

For GitHub Pages, open **Settings → Pages**, choose **GitHub Actions** under **Build and deployment → Source**, and the `Publish AXEZENT research website` workflow will deploy the entire validated site. Do not select “Deploy from a branch” for this version; it would not reconstruct the original calibration STL and photo from the checked-in parts.

This repository intentionally does **not** contain the separate 84.8 MB high-resolution master STL, which was shared privately with the corresponding research authors. All five models are also available in the original complete research package, not all as individual public website downloads.
