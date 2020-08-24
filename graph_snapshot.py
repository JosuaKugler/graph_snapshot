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

def compile(dir, graph_list=default_graph_list):
    """
    creates a new directory if dir doesn't exist
    takes graphs in graph_list and writes their dot code and tikz code to files in dir
    if graph_list isn't explicitly set, it takes default_graph_list
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
        write_dot(graph, filename)
        with open(filename, "r") as f:
            dotgraph = f.read()
        with open(filenametikz, "w") as f:
            options = {'format':"tikz", 'textmode':"math", 'output':filenametikz, 'graphstyle':"scale=0.5, auto", 'tikzedgelabels':True, 'prog':"neato", 'figonly':True, 'force':True}
            f.write(dot2tex.dot2tex(dotgraph, **options))
        
    os.chdir(parentpath)

def beamer_slide(directory, title=None, path=None):
    content = os.listdir(directory)
    texfiles = []
    for filename in content:
        if filename[-4:] == ".tex":
            texfiles.append(filename)
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

print(beamer_slide("test_dir", title="very cool title", path="kruskal_slide.tex"))