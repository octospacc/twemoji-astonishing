#!/bin/sh

echo "[I] Downloading Twemoji files"
wget -O ./twemoji.tar.gz https://github.com/twitter/twemoji/archive/refs/heads/master.tar.gz

echo "[I] Extracting archive"
tar xvf ./twemoji.tar.gz
mv ./twemoji-master ./twemoji

echo "[I] Preparing Pages build"
rm -rf ./public
mkdir -p ./public ./public/Archives
cp ./Build/* ./public/
mkdir -p ./Build/i ./public/i
cp ./twemoji/assets/svg/* ./Build/i/
cp ./twemoji/assets/svg/* ./public/i/
mv ./maxcdn ./public/maxcdn

echo "[I] Making archives"
mv ./Build ./twemoji-astonishing
cd ./public/Archives
7z a -mx9 -mmt$(nproc --all) twemoji-astonishing.zip ../../twemoji-astonishing
7z a -mx9 -mmt$(nproc --all) twemoji-astonishing.7z ../../twemoji-astonishing
tar cvJf twemoji-astonishing.tar.xz ../../twemoji-astonishing
cd ..

echo "[I] Final steps"
tree -I "i|index.html" -H . -o index.html
cd ..
rm -rf ./Build ./twemoji ./twemoji-astonishing ./twemoji.tar.gz
