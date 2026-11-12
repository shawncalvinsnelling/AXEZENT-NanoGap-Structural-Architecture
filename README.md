# AXEZENT NanoGap Structural Architecture

**Research and design: Shawn Calvin Snelling** · Original cube v1.0 (July 2026) · Website release prepared November 11, 2026.

This repository is a **GitHub Pages-ready research website** for the AXEZENT graded gyroid cube, original mathematical generator, selected STL geometry, an original cube CAD render and a photograph of a physical sample shared by the author. The site includes a browser-only mathematical field explorer and explicit validation boundaries.

> **Status:** Geometric model documented; experimental material performance and comparative superiority unverified. The photographed physical sample is not yet linked to complete print/process metadata. A proposed NanoGap wall is not included as a fabricated, validated product.

## Quick start

For Windows users: download the repository ZIP, **extract it**, open `index.html` to preview the visual site locally; note some browsers restrict local downloads when using file://. For full local testing, run `python -m http.server 8000` inside the extracted folder and open http://localhost:8000/ .

## GitHub Pages installation — exact order

1. Sign into GitHub as **`shawncalvinsnelling`**.
2. Create a **new PUBLIC repository** named `AXEZENT-NanoGap-Structural-Architecture`; set the description to `Independent architected-materials research: graded gyroid geometry, NanoGap coupling, STL prototypes, mathematics and validation — Shawn Calvin Snelling.` If uploading this complete folder through the browser, **do not add a template README** at creation.
3. Download and **extract** the supplied site ZIP. Do **not** upload the ZIP as one single file: that will not create a website.
4. Inside the new repository select **Add file → Upload files**. Drag **the contents** of the extracted `AXEZENT-NanoGap-Structural-Architecture` folder into the upload area so `index.html` is at the repository root. Preserve directory structure. Each included file fits GitHub's 25 MiB browser upload limit.
5. Commit to `main` with the message `feat: publish AXEZENT NanoGap architecture research website`.
6. Open **Settings → Pages → Build and deployment**. Select `Deploy from a branch`, `main`, and `/(root)`, then click **Save**.
7. After the Pages deployment completes, open **Settings → Pages → Visit site** and check navigation, downloads, photographs, mobile layout and mathematical explorer.
8. Once the site is live, copy the **actual Pages URL from Settings** to a follow-up email to the researchers.

**Expected URL format after successful publishing:** `https://shawncalvinsnelling.github.io/AXEZENT-NanoGap-Structural-Architecture/` (not live until GitHub actually publishes it).

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

This setup needs no paid host, no Vercel/Netlify, no Node build, and no external JS framework. The site runs on static HTML, CSS and browser JavaScript only.

## Structure

- `index.html` — complete research website
- `assets/images/` — CAD render, actual physical sample photograph and explanatory diagram
- `assets/models/` — calibration STL and outer-frame STL suitable for GitHub browser upload
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
