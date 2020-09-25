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

       git clone https://github.com/jakobus2205/graph_snapshot_pip.git

  2. Change directory to "pygraphviz"

  3.  Run "python setup.py install" to build and install


If you don't have permission to install software on your
system, you can install into another directory using
the --user, --prefix, or --home flags to setup.py.

For example

::

    python setup.py install --prefix=/home/username/python
    or
    python setup.py install --home=~
    or
    python setup.py install --user

If you didn't install in the standard Python site-packages directory
you will need to set your PYTHONPATH variable to the alternate location.
Seehttp://docs.python.org/2/install/index.html#search-path for further details.


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

In addition, you also need these tikzlibraries:

 - arrows
 - shapes
 - decorations














