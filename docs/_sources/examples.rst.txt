Examples
========

A short introduction is to be found in the tutorial section. Here we will provide a thorough example how graph_snapshot can be used.

Following python code takes a given graph G and applies Kruskal's algorithm on it using networkx. In addition two small self-written function isCyclicUtil() and isCyclic() are used, they can be found at the end of the page.

.. code-block:: python

    import networkx as nx
    import graph_snapshot as gs

    edges = [("a","b", {"len": 5}), ("c","b", {"len": 7}), ("a","d", {"len": 3}), ("d","b", {"len": 4}), ("a","c", {"len": 4}), ("a", "f", {"len": 2}), ("b", "f", {"len": 2}), ("c", "f", {"len": 2})]
    G = nx.Graph()
    G.add_edges_from(edges, color = 'black')

    def Kruskal(G): 
        gs.snapshot(G)
        nodes = set(G)
        edges = list(G.edges)
        edges.sort(key = lambda edge: G.edges[edge]["len"]) 
        edges.reverse()

        colorededges = set([])
        while len(colorededges) < len(nodes)-1:
            edge = edges.pop() # lowest weight
            testedges = colorededges.copy()
            testedges.add(edge)
            if not isCyclic(nx.Graph(list(testedges))): 
                colorededges.add(edge)
                G.edges[edge]['color'] = 'red'
                gs.snapshot(G)
    
    Kruskal(G)

    gs.compile("test_dir", scale_total=0.8, scale_edge_lengths=1, orientation = "0", overlap = "false", splines = "true",sep = "0")
    gs.beamer_slide("test_dir", title="very cool title", path="kruskal_slide.tex", caption_list=["A","B","D"])
    gs.latex_document("test_dir", title="very cool title", path="testkruskal2.tex", caption_list=["A","B","D"])


In the first line of the Kruskal function a snapshot of the unmodified graph is taken. Then after each step of the algorithm a new snapshot of the modified Graph is taken by calling

    >>> gs.snapshot(G)

After calling the Kruskal function each taken snapshot is converted into tikz code in a own graph<i>.tex file and placed into the directory "test_dir" by simply calling

    >>> gs.compile("test_dir", scale_total=0.8, scale_edge_lengths=1, orientation = "0", overlap = "false", splines = "true",sep = "0")

The meaning of the additional options can be found in the reference section. The "test_dir" directory looks as follows: 

.. code-block:: console

    $ ls directory_where_you_want_the_tikz_files
    graph0.dot  graph0.tex  graph1.dot  graph1.tex  graph2.dot  graph2.tex  graph3.dot  graph3.tex  graph4.dot  graph4.tex

After filling the "test_dir" directory with .tex files containing tikz-code we modify a given epmty .tex file to a beamer frame that can be included in a beamer presentation by calling

    >>> gs.beamer_slide("test_dir", title="very cool title", path="kruskal_slide.tex", caption_list=["A","B","D"])

The beamer_slide function takes all "graph<i>.tex" files from the "test_dir" directory and includes them in the empty "kruskal_slide.tex" file creating a beamer_slide, entitles the frame with "very cool title" and captions the first three images. Content of "kruskal_slide.tex" after running:

.. code-block:: tex

    \begin{frame}
    \frametitle{very cool title}
    \only<1>{\begin{figure} \input{test_dir/graph0.tex} \caption{A} \end{figure}}
    \only<2>{\begin{figure} \input{test_dir/graph1.tex} \caption{B} \end{figure}}
    \only<3>{\begin{figure} \input{test_dir/graph2.tex} \caption{D} \end{figure}}
    \only<4>{\begin{figure} \input{test_dir/graph3.tex} \end{figure}}
    \only<5>{\begin{figure} \input{test_dir/graph4.tex} \end{figure}}
    \end{frame}

Similar to the beamer_slide function the latex_document modifies a given empty .tex file to a compilable latex document by calling:

    >>> gs.latex_document("test_dir", title="very cool title", path="testkruskal2.tex", caption_list=["A","B","D"])

The latex_document function takes all "graph<i>.tex" files from the "test_dir" directory and includes them in the empty "testkruskal2.tex" file creating a latex document, entitles the document with "very cool title" and captions the first three images. Content of "testkruskal2.tex" after running:

.. code-block:: tex
    
    \documentclass{article}
    \usepackage{tikz}
    \usetikzlibrary{decorations,arrows,shapes}
    \usepackage{amsmath}
    \usepackage{float}


    \begin{document}


    \section{very cool title}
    \begin{figure}[H] \input{test_dir/graph0.tex} \caption{A} \end{figure}
    \begin{figure}[H] \input{test_dir/graph1.tex} \caption{B} \end{figure}
    \begin{figure}[H] \input{test_dir/graph2.tex} \caption{D} \end{figure}
    \begin{figure}[H] \input{test_dir/graph3.tex} \end{figure}
    \begin{figure}[H] \input{test_dir/graph4.tex} \end{figure}


    \end{document}

As promised the code of the functions isCyclicUtil() and isCyclic():

.. code-block:: python
    
    def isCyclicUtil(G, v, visited, parent):
        visited[v] = True
        for i in G.neighbors(v): 
            # If the node is not visited then recurse on it 
            if  visited[i]==False:
                if(isCyclicUtil(G,i,visited,v)): 
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif  parent!=i:
                return True
        return False

    def isCyclic(G): #gleich wie Tiefensuche, im Idealfall O(V+E)
        visited = {}
        for node in G.nodes():
            visited[node] = False

        for i in G.nodes(): 
            if visited[i] ==False:
                if(isCyclicUtil(G, i,visited,list(G.nodes())[-1]))== True: 
                    return True

        return False