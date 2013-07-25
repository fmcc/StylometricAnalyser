import networkx as nx
import numpy as np
import string

dt = [('len', float)]
A = np.array()    
A = A.view(dt)

G = nx.from_numpy_matrix(A)

labels = dict(zip(G.nodes(),labels))
G = nx.relabel_nodes(G, labels)    

G = nx.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color=None, width="2.0")

G.draw('./out.png', format='png', prog='neato')
