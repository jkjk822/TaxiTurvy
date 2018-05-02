import matplotlib.pyplot as plt
import networkx as nx
import json
from streetMapParser import buildRoadGraph, snapToGraph
#from portugalTaxiParser import parseTrips
from beijingparse import parseTrips
import numpy as np
from graph import save_graph

# Portugal Parse
#trips = parseTrips('SamplePorto.txt')

#graph, edgeTable = buildRoadGraph('portoMap.xml')
#print("built")
trips = {}
with open("beijingSnappedTrips.json", 'r') as f:
	trips = json.loads(f.read())
print("loaded")

nx.draw(trips)
nx.write_gexf(trips, "beijing.gexf")
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