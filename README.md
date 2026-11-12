# AXEZENT NanoGap Structural Architecture

**Research and design: Shawn Calvin Snelling** · Original cube v1.0 (July 2026) · Website release prepared November 11, 2026.

This repository is a **GitHub Pages-ready research website** for the AXEZENT graded gyroid cube, original mathematical generator, selected STL geometry, an original cube CAD render and a photograph of a physical sample shared by the author. The site includes a browser-only mathematical field explorer and explicit validation boundaries.

> **Status:** Geometric model documented; experimental material performance and comparative superiority unverified. The photographed physical sample is not yet linked to complete print/process metadata. A proposed NanoGap wall is not included as a fabricated, validated product.

## Quick start

The repository is already published at `https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture`. After cloning or downloading the repository, run `python scripts/reassemble_assets.py` to reconstruct the original printed-cube photograph and calibration STL, verifying their SHA-256 values. Open `index.html` or run `python -m http.server 8000` for a local preview.

## GitHub Pages — one-time setting

1. Open this repository's **Settings → Pages**.
2. Under **Build and deployment → Source**, select **GitHub Actions** (not “Deploy from a branch”).
3. Open **Actions → Publish AXEZENT research website**. The workflow reconstructs the exact source assets, verifies the files, runs five tests, and deploys GitHub Pages automatically on every push to `main`.
4. After deployment succeeds, use the **Visit site** link in Pages settings to confirm the live address.

The expected URL is `https://shawncalvinsnelling.github.io/AXEZENT-NanoGap-Structural-Architecture/`; it should not be treated as live until deployment succeeds.

### Alternative using Git CLI (Windows PowerShell)

```powershell
# After the empty repository is created on GitHub:
cd "C:\path\to\AXEZENT-NanoGap-Structural-Architecture"
git init
git branch -M main
git add .
git commit -m "feat: publish AXEZENT NanoGap architecture research website"
git remote add origin https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture.git
git push -u origin main
```

This setup needs no paid host, no Vercel/Netlify, no Node build, and no external JS framework. The public site runs on static HTML, CSS and browser JavaScript; GitHub Actions reconstructs the large source assets before deployment.

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

See `docs/RIGHTS_AND_USE.md` before uploading: a public website and source directory disclose the visible equations and model files. No open-source license is implied by default.

### Optional Windows publishing helper

After creating the empty GitHub repository, run `PUBLISH_TO_GITHUB_WINDOWS.bat` from the extracted folder if you have Git for Windows installed. It explicitly asks you to type `PUBLISH` before uploading any contents. GitHub authentication must already be configured.


## Binary asset fidelity and automated publishing

The full-size **original 38.1 mm calibration STL** and **full-resolution printed-cube photograph** are preserved *losslessly* as chunks in `data/asset-parts/` to make the initial GitHub transfer reliable. This is not a change to the original geometry. `scripts/reassemble_assets.py` combines the chunks, verifies their original SHA-256 hashes, and writes the exact files to the documented asset paths. The Actions build runs this step before validation and deployment. Run the same script locally after cloning to obtain all original research-site assets.

For GitHub Pages, open **Settings → Pages**, choose **GitHub Actions** under **Build and deployment → Source**, and the `Publish AXEZENT research website` workflow will deploy the entire validated site. Do not select “Deploy from a branch” for this version; it would not reconstruct the original calibration STL and photo from the checked-in parts.

This repository intentionally does **not** contain the separate 84.8 MB high-resolution master STL, which was shared privately with the corresponding research authors. All five models are also available in the original complete research package, not all as individual public website downloads.
