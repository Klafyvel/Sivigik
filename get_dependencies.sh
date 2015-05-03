#! /bin/bash

mkdir tmp
cd tmp
# get the js tools (source-code highlight + jquery)
wget http://yandex.st/highlightjs/8.0/highlight.min.js
wget http://highlightjs.org/static/styles/atelier-dune.dark.css
wget http://code.jquery.com/jquery-1.7.1.min.js
pip install --user django_mobile

cp highlight.min.js ../article/static/article
cp atelier-dune.dark.css ../article/static/article
cp jquery-1.7.1.min.js ../utils/static/
# get the images
wget https://i.creativecommons.org/l/by/4.0/80x15.png
cp 80x15.png ../utils/static/
cd ../
rm -r tmp
