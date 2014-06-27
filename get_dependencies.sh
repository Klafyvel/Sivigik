#! /bin/bash

mkdir tmp
cd tmp
# get the js tools (source-code highlight)
wget http://yandex.st/highlightjs/8.0/highlight.min.js
wget http://highlightjs.org/static/styles/atelier-dune.dark.css

cp highlight.min.js ../article/static/article
cp atelier-dune.dark.css ../article/static/article

cd ../
rm -r tmp