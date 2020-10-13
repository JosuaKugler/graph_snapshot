**********
Installing
**********

Quick Install
=============

Get graph_snapshot from the Python Package Index at
http://pypi.python.org/pypi/graph_snapshot

or install it with::

   pip install graph_snapshot

to get the latest stable version.


Installing from Source
======================


Github
------

  1. Clone the pygraphviz repository

       git clone https://github.com/NicoHaaf/graph_snapshot_pip.git

  2. Change directory to "graph_snapshot_pip"

  3.  Run "python setup.py install" to build and install



Requirements
============

Python
------

graph_snapshot works only with Python 3.8.

You need some python further python packages::

    pip install networkx
    pip install pygraphviz #depends on graphviz
    pip install dot2tex



GraphViz
--------

To use PyGraphviz you need GraphViz version 2.16 or later.
Some versions have known bugs that have been fixed; get the latest
release available for best results.

 - Official site: http://www.graphviz.org


Latex
-----

In order to compile the output files of graph_snapshot, the following Latex packages are required.

 - amsmath
 - tikz
 - float

In addition, you also need these tikzlibraries:

 - arrows
 - shapes
 - decorations

