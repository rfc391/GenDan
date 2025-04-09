#!/bin/bash

set -e

APP_NAME="gendan"
VERSION="1.0.0"
DIST_DIR="dist"

echo "[+] Cleaning previous builds..."
rm -rf build/ $DIST_DIR/ __pycache__/

echo "[+] Creating dist directory..."
mkdir -p $DIST_DIR

echo "[+] Packaging .deb..."
fpm -s python -t deb     --name $APP_NAME     --version $VERSION     --description "GenDan - Genetic Intelligence Suite"     --maintainer "rfc391@github"     --license "MIT"     --url "https://github.com/rfc391"     --architecture all     --prefix /opt/$APP_NAME     --deb-no-default-config-files     .

echo "[+] Creating AppImage (requires appimagetool)..."
if command -v appimagetool &> /dev/null; then
    mkdir -p AppDir/usr/bin
    cp -r *.py AppDir/usr/bin/
    cp requirements.txt AppDir/
    (cd AppDir && appimagetool . ../$DIST_DIR/$APP_NAME.AppImage)
else
    echo "[-] appimagetool not found. Skipping AppImage build."
fi

echo "[+] Done. Artifacts in $DIST_DIR/"
