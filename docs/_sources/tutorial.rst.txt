Tutorial
========


Preliminaries
-------------

In order to use the graph_snapshot package, a basic knowledge of the :ref:`networkx Graph <networkx:Graph>` concept ist required.
So make sure to be able to work with graphs.

Workflow
--------

First, import networkx and graph_snapshot and create a Graph::

    >>> import networkx as nx 
    >>> import graph_snapshot as gs
    >>> G = nx.Graph()

Now, do something with the graph, e.g. add edges or perform an algorithm::

    >>> edges = [("a","b", {"len": 5}), ("c","b", {"len": 7}), ("a","d", {"len": 3}), ("d","b", {"len": 4}), ("a","c", {"len": 4}), ("a", "f", {"len": 2}), ("b", "f", {"len": 2})]
    >>> G.add_edges_from(edges, color = 'black')

Everytime you want the current state of the algorithm to be visualized, you can 'snapshot' the graph::

    >>> gs.snapshot(G)
    >>> G.add_edge("c", "f", len = 2, color = 'red')
    >>> gs.snapshot(G)

Once you are done with your algorithm, it is time to create the tikz code from your snapshots::

    >>> gs.compile("directory_where_you_want_the_tikz_files", lenAsLabel = True)

The directory should look as follows: 

.. code-block:: console

    $ ls directory_where_you_want_the_tikz_files
    graph0.dot  graph0.tex  graph1.dot  graph1.tex

You can then manually include the tex files into your document. The following two images are created by calling::

    >>> gs.standalone("directory_where_you_want_the_tikz_files")


.. tikz:: [>=latex,line join=bevel,scale=1, auto, every node/.style={transform shape}] \node (a) at (101.02bp,141.67bp) [draw,circle] {$a$};
  \node (b) at (216.6bp,198.18bp) [draw,circle] {$b$};
  \node (c) at (18.0bp,18.0bp) [draw,circle] {$c$};
  \node (d) at (76.363bp,254.03bp) [draw,circle] {$d$};
  \node (f) at (177.69bp,135.62bp) [draw,circle] {$f$};
  \draw [black,] (a) ..controls (139.55bp,160.51bp) and (178.11bp,179.36bp)  .. node {$5$} (b);
  \draw [black,] (a) ..controls (74.905bp,102.77bp) and (44.248bp,57.101bp)  .. node {$4$} (c);
  \draw [black,] (a) ..controls (92.495bp,180.51bp) and (84.86bp,215.31bp)  .. node {$3$} (d);
  \draw [black,] (a) ..controls (131.41bp,139.27bp) and (147.45bp,138.01bp)  .. node {$2$} (f);
  \draw [black,] (b) ..controls (167.17bp,153.33bp) and (67.871bp,63.245bp)  .. node {$7$} (c);
  \draw [black,] (b) ..controls (172.73bp,215.65bp) and (120.33bp,236.52bp)  .. node {$4$} (d);
  \draw [black,] (b) ..controls (200.95bp,173.02bp) and (193.21bp,160.57bp)  .. node {$2$} (f);

.. tikz:: [>=latex,line join=bevel,scale=1, auto, every node/.style={transform shape}]\node (a) at (18.0bp,143.38bp) [draw,circle] {$a$};
  \node (b) at (142.92bp,136.8bp) [draw,circle] {$b$};
  \node (c) at (75.143bp,18.0bp) [draw,circle] {$c$};
  \node (d) at (45.066bp,253.35bp) [draw,circle] {$d$};
  \node (f) at (78.613bp,94.045bp) [draw,circle] {$f$};
  \draw [black,] (a) ..controls (59.848bp,141.17bp) and (101.04bp,139.0bp)  .. node {$5$} (b);
  \draw [black,] (a) ..controls (36.422bp,102.96bp) and (56.718bp,58.426bp)  .. node {$4$} (c);
  \draw [black,] (a) ..controls (27.399bp,181.57bp) and (35.682bp,215.22bp)  .. node {$3$} (d);
  \draw [black,] (a) ..controls (41.85bp,123.97bp) and (54.855bp,113.38bp)  .. node {$2$} (f);
  \draw [black,] (b) ..controls (120.77bp,97.974bp) and (97.066bp,56.427bp)  .. node {$7$} (c);
  \draw [black,] (b) ..controls (112.48bp,173.05bp) and (75.483bp,217.12bp)  .. node {$4$} (d);
  \draw [black,] (b) ..controls (117.43bp,119.85bp) and (103.97bp,110.9bp)  .. node {$2$} (f);
  \draw [red,] (c) ..controls (76.514bp,48.056bp) and (77.234bp,63.827bp)  .. node {$2$} (f);

If you want to include the tex files into your beamer class documentation you can instead use following to create a beamer slide containing all images:

    >>> gs.beamer_slide("directory_where_you_want_the_tikz_files")

To create a single latex document containg all images call:

    >>> gs.latex_document("directory_where_you_want_the_tikz_files")

The last two mentioned functions also provide several options, including: setting a title for the created beamer slide or latex document, define a path where the generated latex files will be placed or caption your images by providing a caption list as following:

    >>> gs.beamer_slide("directory_where_you_want_the_tikz_files", "title", "directory_where_returndes_tex_file_is_placed", ["caption1","cpation2"])
    >>> gs.latex_document("directory_where_you_want_the_tikz_files", "title", "directory_where_returndes_tex_file_is_placed", ["caption1","cpation2"])

Configuration
-------------

Using multiple "Screenshot series": `graph_list`
************************************************

Sometimes you might want to visualize two algorithms in the same file.
Then you should make use of the `graph_list` concept. First, specify a list for each algorithm::

    >>> algorithm1_list = []
    >>> algorithm2_list = []

When calling `gs.snapshot`, decide for one list, e.g.::

    >>> gs.snapshot(G, graph_list = algorithm1_list)

Finally, you can compile each list on it's own::

    >>> gs.compile("algorithm1_dir", graph_list = algorithm1_list)
    >>> gs.compile("algorithm2_dir", graph_list = algorithm2_list)


Keywordarguments for Edges/Nodes
********************************

As you have already seen, you can pass keywordarguments to graph edges. The same concept works for nodes as well.
Any keyword that is understandable by tikz will have an effect on the resulting image.
If you want to add specific style to your edges, you can also define your own tikz style in the document header and use that style as an edge attribute.
There are also some edge keywords that have specific meaning.

* `len` specifies the length of the edge. The graph layout algorithm will try to fit this lenght as close as possible, but as you can see in the second figure of the last section, if you hurt the triangle inequality, this can't work.

* `weight` specifies how much this edge is considered in computing the layout. In general, this option will not be needed.

* `label` has the same meaning as in tikz, however it can be overwritten by the len argument if you set `lenAsLabel = True` when calling the compile function.


Keywordarguments for `compile` 
******************************

We have already mentioned the `graph_list` and `lenAsLabel` keywords in the previous two subsections. See the reference for a detailed description of the other arguments.