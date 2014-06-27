#! /bin/bash

mkdir tmp
cd tmp
# get the js tools (mathjax and source-code highlight)
wget https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML -O mathjax.js
wget http://yandex.st/highlightjs/8.0/highlight.min.js
wget http://highlightjs.org/static/styles/atelier-dune.dark.css

cp mathjax.js ../article/static/article
cp highlight.min.js ../article/static/article
cp atelier-dune.dark.css ../article/static/article

cd ../
rm -r tmp