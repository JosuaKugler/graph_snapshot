import networkx as nx
import graph_snapshot as gs

G = nx.Graph()

edges = [("a","b", {"len": 5}), ("c","b", {"len": 7}), ("a","d", {"len": 3}), ("d","b", {"len": 4}), ("a","c", {"len": 4}), ("a", "f", {"len": 2}), ("b", "f", {"len": 2})]
G.add_edges_from(edges, color = 'black')

gs.snapshot(G)
G.add_edge("c", "f", len = 2, color = 'red')
gs.snapshot(G)

gs.compile("directory_where_you_want_the_tikz_files", lenAsLabel=True)

gs.standalone("directory_where_you_want_the_tikz_files")