# Exact GitHub setup order

This site uses **GitHub Pages ONLY**. No other web hosting services are required. Repository target: `shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture`.

1. Go to https://github.com/new while logged into `shawncalvinsnelling`.
2. Owner: `shawncalvinsnelling`.
3. Repository name: `AXEZENT-NanoGap-Structural-Architecture`.
4. Description: `AXEZENT architected metamaterial research — graded gyroid cube, NanoGap geometry, STL, mathematics, and validation | Shawn Calvin Snelling`.
5. Visibility: **Public** (required for a broadly accessible research site on free GitHub Pages).
6. Do not initialize with a GitHub README, license, or gitignore (the folder has these or deliberately does not include a license).
7. Choose **Create repository**.
8. On the empty repo, choose **uploading an existing file**, or **Add file → Upload files**.
9. On your computer, unzip the provided **SITE GITHUB ZIP**. Open the extracted folder and select its **contents** (not the enclosing directory or ZIP) for upload. Folder drag-and-drop works in the GitHub browser uploader; preserve subfolders, including `.nojekyll`. The packaged individual files are all below GitHub's 25 MiB browser limit.
10. Commit onto **main**.
11. Go to **Settings → Pages**.
12. Under **Build and deployment**, choose **Deploy from a branch**.
13. Select **main** and **/(root)**; click **Save**.
14. Once GitHub reports deployment success, click **Visit site**. Check images, mathematical sliders, gallery, STL links, research PDF, and mobile navigation.
15. In the GitHub repository About panel set the website field to the **actual URL displayed by Pages**; only then email that link to the researchers.

**Important:** The public repo exposes the original Python generator, equations, some STL models and a sample photograph; do not publish files you wish to keep confidential. The high-resolution 84.8 MB master is intentionally omitted from the public repo but was separately shared with the researchers.

For browser upload, GitHub limits each individual file to 25 MiB. The ZIP file itself is **not** uploaded to GitHub as the website; its unzipped content is uploaded. For larger files, GitHub recommends Git command-line uploads (up to its 100 MiB Git hard limit) or Git LFS.

Troubleshooting: if the site shows README text rather than the styled website, confirm `index.html` is at repository root and Pages source is main/root; if images fail, check that paths retain the exact case and directories; if zip downloads fail, check browser file links after upload.
