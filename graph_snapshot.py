import networkx as nx
#import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot
import pygraphviz
import dot2tex
import copy
import os

default_graph_list = []

def snapshot(G,graph_list=default_graph_list):
    """
    takes a given graph G and appends it to graph_list.
    If no graph_list is given, it is appended to a global list
    """
    H = copy.deepcopy(G)
    graph_list.append(H)

def setlabelweight(G, scale_edge_lengths):
    for edge in G.edges():
        try:
            G.edges[edge]['label'] = G.edges[edge]['weight']
            G.edges[edge]['len'] = 0.5 * scale_edge_lengths * G.edges[edge]['weight']
            G.edges[edge]['weight'] = 1
        except:
            print("no weights given")
            pass

def compile(dir, graph_list=default_graph_list, label_with_weight=True, scale_total = 1, scale_edge_lengths = 1):
    """
    creates a new directory if dir doesn't exist
    takes graphs in graph_list and writes their dot code and tikz code to files in dir
    if graph_list isn't explicitly set, it takes default_graph_list
    label_with_weight: add edge weight as label
    --------------------------------------------------------------------------
    options:
    see https://dot2tex.readthedocs.io/en/latest/usage_guide.html
    """
    parentpath = os.getcwd()
    try:
        os.chdir(dir)
    except:
        os.mkdir(dir)
        os.chdir(dir)
    for index, graph in enumerate(graph_list):
        filename = 'graph' + str(index) + '.dot'
        filenametikz = 'graph' + str(index) + '.tex'
        if label_with_weight:
            setlabelweight(graph, scale_edge_lengths)   
        write_dot(graph, filename)
        with open(filename, "r") as f:
            dotgraph = f.read()
        with open(filenametikz, "w") as f:
            options = {'format':"tikz", 'textmode':"math", 'output':filenametikz, 'graphstyle':"scale=" + str(scale_total) + ", every node/.style={transform shape}", 'tikzedgelabels':False, 'prog':"neato", 'figonly':True, 'force':True}
            f.write(dot2tex.dot2tex(dotgraph, **options))
        
    os.chdir(parentpath)

def beamer_slide(directory, title=None, path=None):
    content = os.listdir(directory)
    texfiles = []
    index = 0
    next = True
    while next:
        nextfile = f"graph{index}.tex"
        if nextfile in content:
            texfiles.append(nextfile)
            index += 1
        else:
            next = False
    slidelines = [r"\begin{frame}"]
    if title:
        slidelines.append(r"\frametitle{" + title + r"}")
    for i, texfile in enumerate(texfiles):
        filerawname = texfile.split(".")[0]
        filenamewithdir = os.path.join(directory, filerawname)
        line = r"\only<" + str(i+1) + r">{\input{" + filenamewithdir + r".tex}}"
        slidelines.append(line)
    slidelines.append(r"\end{frame}")
    slidecode = ""
    for line in slidelines:
        slidecode += line + "\n"
    if path:
        with open(path, "w") as f:
            f.write(slidecode)
    return slidecode