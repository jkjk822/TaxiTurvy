# Windows Linux subsystem workarounds
import matplotlib
matplotlib.use('Agg')
# Windows Linux subsystem workarounds
import matplotlib.pyplot as plt
import networkx as nx
import json
from streetMapParser import buildRoadGraph, snapToGraph
from portugalTaxiParser import parseTrips


graph, edgeTable = buildRoadGraph('portoMap.xml')
# print(nx.number_weakly_connected_components(graph))
# print(len(graph.edges))
# for c in nx.weakly_connected_components(graph):
# 	print(len(graph.subgraph(c)))
print("built")
#Read in trips using:
trips = {}
with open("portoSnappedTrips.json", 'r') as f:
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
# trips = parseTrips('portoTaxi.csv')
# print("parsed")
# graph, edgeTable = buildRoadGraph('portoMap.xml')
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

