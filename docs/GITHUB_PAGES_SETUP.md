# Current GitHub Pages operations

**Research author:** Shawn Calvin Snelling  
**Repository:** https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture

## Confirmed status

The project was uploaded to `main` and the GitHub Actions **Publish AXEZENT research website** workflow completed its build and deployment successfully on November 11, 2026 (US Central time). Previous instructions to create a new repository or select branch-based Pages are obsolete.

- Repository: https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture
- Website to check: https://shawncalvinsnelling.github.io/AXEZENT-NanoGap-Structural-Architecture/
- Pages settings: https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture/settings/pages
- Workflow: https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture/actions/workflows/pages.yml

**Deployment source must remain GitHub Actions**. Branch-based Pages would not reconstruct the original calibration STL and full-resolution photographed-cube image from the committed asset parts.

## Reproduction

```powershell
python scripts/reassemble_assets.py
python -m unittest discover -s tests -v
python -m http.server 8000
```

Open `http://localhost:8000/` and check gallery, navigation, equation explorer, downloadable files, and the site on mobile.

If the site needs redeployment, go to the Actions tab, select the **Publish AXEZENT research website** workflow, and use **Run workflow**. Check the result and the Pages link before emailing researchers.

The original 84.8 MB high-resolution master STL is not published in this repository; it was shared separately with the corresponding research authors. The public repository **does** include mathematical generator source and selected STL geometry. If patentability, secrecy or commercialization is contemplated, seek professional advice about disclosure before releasing additional source material.

**Research status:** the mathematical geometry is documented, but comparative material strength is unverified.
