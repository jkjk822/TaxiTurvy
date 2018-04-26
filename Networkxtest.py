# Quick test script for networkx initialization

from xml.etree import ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt

#G = nx.Graph()
#G.add_node(1)
#G.add_nodes_from([2, 3])
#G.add_edge(1, 2)
#e = (2, 3)
#G.add_edge(*e)


DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
DG.out_degree(1, weight='weight')

DG.degree(1, weight='weight')

list(DG.successors(1))

list(DG.neighbors(1))


#plt.subplot(121)
nx.draw(DG, with_labels=True, font_weight='bold')
#plt.subplot(122)
#nx.draw_shell(DG, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()