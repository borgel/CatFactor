CatFactor
=========
Scrapes wikipedia articles for (cat) facts, then emails them.

Design Choices
--------------
- Which sentence to use? It looks like the first sentence includes the subject, which makes it very clear what's going on. So lets use that

Usage
====
catFactor
- # sentences to pull
- max # of layers down to go

Installation
------------
pip install nltk, wikipedia

MUST run 'nltk.download()' and download the 'punkt' tokenizer. You will find
it in the 'Modules' section.


Resources
=========
- http://docs.python.org/2/library/argparse.html#module-argparse
