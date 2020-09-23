#test script for graph_snapshot.py
import networkx as nx
import graph_snapshot as gs

edges = [("a","b", 5), ("c","b", 7), ("a","d", 3), ("d","b", 4), ("a","c", 4), ("d", "e", 3), ("a", "e", 5), ("a", "f", 2), ("b", "f", 2), ("c", "f", 5)]

edges2 = [("a","b", {"len": 5}), ("c","b", {"len": 7}), ("a","d", {"len": 3}), ("d","b", {"len": 4}), ("a","c", {"len": 4}), ("a", "f", {"len": 2}), ("b", "f", {"len": 2}), ("c", "f", {"len": 2})]

G = nx.Graph()
G.add_edges_from(edges2, color = 'black')
#G.add_weighted_edges_from(edges, color = 'black')

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

def Kruskal(G): # in dieser Implementierung O(E*(E + V)), optimal ist O(E log E)
    gs.snapshot(G)
    nodes = set(G)
    edges = list(G.edges)
    edges.sort(key = lambda edge: G.edges[edge]["len"]) # O(E log E)
    edges.reverse()
    
    colorededges = set([])
    while len(colorededges) < len(nodes)-1:
        edge = edges.pop() # lowest weight
        testedges = colorededges.copy()
        testedges.add(edge)
        if not isCyclic(nx.Graph(list(testedges))): # isCyclic: <= O(V + E)
            colorededges.add(edge)
            G.edges[edge]['color'] = 'red'
            gs.snapshot(G)

        
        

        

print(G.nodes)

Kruskal(G)

gs.compile("test_dir", scale_total=0.8, scale_edge_lengths=1, orientation = "0", overlap = "false", splines = "true",sep = "0")
gs.beamer_slide("test_dir", title="very cool title", path="kruskal_slide.tex", caption_list=["A","B","D"])
gs.latex_document("test_dir", title="very cool title", path="testkruskal2.tex", caption_list=["A","B","D"])