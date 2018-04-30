# Windows Linux subsystem workarounds
#import matplotlib
#matplotlib.use('Agg')
# Windows Linux subsystem workarounds
import matplotlib.pyplot as plt
import networkx as nx
import json
from streetMapParser import buildRoadGraph, snapToGraph
from beijingparse import parseTrips


graph, edgeTable = buildRoadGraph('beijingmap.xml')
# print(nx.number_weakly_connected_components(graph))
# print(len(graph.edges))
# for c in nx.weakly_connected_components(graph):
# 	print(len(graph.subgraph(c)))
print("built")
#Read in trips using:
trips = {}
with open("beijingSnappedTrips.json", 'r') as f:
	trips = json.loads(f.read())
print("loaded")
for tripID in trips:
	path = []
	prev = None
	for nodeID in trips[tripID]:
		print(nodeID in graph)
		if prev:
			path += nx.bidirectional_dijkstra(graph, prev, nodeID)[1]
		prev = nodeID
	print(path)
	print(nx.bidirectional_dijkstra(graph, trips[tripID][0], trips[tripID][-1])[1])
	print()

#
# For resnapping
#
# trips = beijingTrips()
# print("parsed")
# graph, edgeTable = buildRoadGraph('beijingMap.xml')
# print("built")
# trips, error = snapToGraph(trips, graph)
# print("snapped")
# with open("portoSnappedTrips.json", 'w') as f: # encode for later use
# 	f.write(json.dumps(trips, indent=4))
# print("wrote to file")
# print(error)

#for u, v, keys, dist in graph.edges(data='dist', keys=True):
#	print(dist)
# nx.draw(graph)
# plt.savefig('test.pdf')

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


#G.layout()
#G.draw("test.ps")
#nx.draw(G, pos, with_labels=True)
#plt.show()