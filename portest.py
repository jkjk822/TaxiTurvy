import matplotlib.pyplot as plt
import networkx as nx
import json
from streetMapParser import buildRoadGraph, snapToGraph
from portugalTaxiParser import parseTrips
#from beijingparse import parseTrips
import numpy as np

# Portugal Parse
#trips = parseTrips('SamplePorto.txt')

graph, edgeTable = buildRoadGraph('portoMap.xml')
print("built")

colors = [
	{'color': {'r': 255, 'g': 102, 'b': 102, 'a': 0}},
	{'color': {'r': 255, 'g': 0, 'b': 0, 'a': 0}},
	{'color': {'r': 153, 'g': 76, 'b': 0, 'a': 0}},
	{'color': {'r': 255, 'g': 128, 'b': 0, 'a': 0}},
	{'color': {'r': 255, 'g': 255, 'b': 204, 'a': 0}},
	{'color': {'r': 255, 'g': 255, 'b': 0, 'a': 0}},
	{'color': {'r': 102, 'g': 102, 'b': 255, 'a': 0}},
	{'color': {'r': 0, 'g': 0, 'b': 255, 'a': 0}},
	{'color': {'r': 255, 'g': 153, 'b': 204, 'a': 0}},
	{'color': {'r': 255, 'g': 0, 'b': 127, 'a': 0}},
	{'color': {'r': 0, 'g': 153, 'b': 153, 'a': 0}},
	{'color': {'r': 0, 'g': 255, 'b': 255, 'a': 0}},
	{'color': {'r': 0, 'g': 102, 'b': 0, 'a': 0}},
	{'color': {'r': 0, 'g': 255, 'b': 0, 'a': 0}},
]
with open("pathsToColor.json", 'r') as f:
	count = 0
	i = 0
	for line in f:
		if count%4 == 0:
			print(line)
		elif count%4 == 1 or count%4 == 2:
			for node in json.loads(line):
				graph.node[node]['viz'] = colors[i]
				print(graph.node[node])
			i+=1
		count += 1
print("loaded")

# nx.draw(trips)
nx.write_gexf(graph, "porto.gexf")
#save_graph(trips,"test.pdf")


##############
# Plot each coordinate as a node, and then draw

# Initialize NetworkX 
#G = nx.MultiDiGraph()

# Initialize PyGraphviz
#G = pgv.AGraph()


# Add nodes from dict
#G.add_nodes_from(pos.keys())
#G.add_edges_from([(0,1), (1,2), (2,3)])

# Convert NetworkX to PyGraphviz 
#G = nx.nx_agraph.to_agraph(G)

# Draw and plot

# Pygraphviz
#G.layout()
#G.draw("test.ps")

# NetworkX
#nx.draw(G, pos, with_labels=True)
#nx.write_gexf(G, "test.gexf")

# Plotting
#plt.show()