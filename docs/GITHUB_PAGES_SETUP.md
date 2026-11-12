# GitHub Pages — current repository setup

**Research author:** Shawn Calvin Snelling

**Repository:** https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture

The complete website source is committed to the repository's `main` branch. You do **not** need to create or upload the repository again.

## One-time GitHub Pages activation

1. Open the repository and select **Settings**.
2. Open **Pages** in the left-hand sidebar.
3. Under **Build and deployment → Source**, select **GitHub Actions**.
4. Open **Actions → Publish AXEZENT research website**, and rerun the workflow if the earlier run failed. New commits to `main` also trigger it automatically.
5. Once deployment reports success, use **Settings → Pages → Visit site**. Check the mathematical explorer, the physical print and CAD photographs, downloadable STL files, PDF, and mobile layout.

Expected published URL: `https://shawncalvinsnelling.github.io/AXEZENT-NanoGap-Structural-Architecture/` (verify GitHub reports successful deployment before sharing).

## Why Actions instead of branch mode?

The original 38.1 mm calibration STL and full-resolution source photograph are stored losslessly as parts in `data/asset-parts/`. The workflow invokes `python scripts/reassemble_assets.py`, validates their SHA-256 hashes against the manifest, runs five repository checks, and generates the full static Pages artifact. Branch mode would not reassemble these assets.

To preview locally after cloning:

```powershell
python scripts/reassemble_assets.py
python -m unittest discover -s tests -v
python -m http.server 8000
```

Then visit `http://localhost:8000/`.

The original 84.8 MB high-resolution master cube STL was not made public in this repository; it was supplied directly to the research team. Public source is attributed to Shawn Calvin Snelling. Research performance remains unverified.
