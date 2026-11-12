@echo off
setlocal EnableExtensions
cd /d "%~dp0"
echo.
echo AXEZENT NanoGap Structural Architecture
 echo Author: Shawn Calvin Snelling
 echo.
echo STEP 1: First create the empty public repository here:
echo https://github.com/new
 echo Repository name: AXEZENT-NanoGap-Structural-Architecture
echo.
echo This repository contains original scientific mathematics, Python source, and selected STL models.
echo Publishing it makes those files publicly accessible.
echo.
where git >nul 2>&1
if errorlevel 1 (
  echo Git was not found on this computer. Install Git for Windows, then rerun this batch file.
  pause
  exit /b 1
)
set /p CHOICE=After creating the GitHub repository, type PUBLISH to continue: 
if /I not "%CHOICE%"=="PUBLISH" (
  echo Cancelled. Nothing was uploaded.
  pause
  exit /b 0
)
if not exist .git (
  git init
)
git branch -M main
git add .
git commit -m "feat: publish AXEZENT NanoGap architecture research website"
git remote get-url origin >nul 2>&1
if errorlevel 1 (
  git remote add origin https://github.com/shawncalvinsnelling/AXEZENT-NanoGap-Structural-Architecture.git
)
git push -u origin main
if errorlevel 1 (
  echo Push failed. Please verify the repository exists and GitHub authentication is configured.
  pause
  exit /b 1
)
echo.
echo Git push completed. To activate the website:
echo 1. Open GitHub repository ^> Settings ^> Pages.
echo 2. Choose Deploy from a branch / main / root. Save.
echo 3. Open the published URL from GitHub Pages settings.
echo.
pause
