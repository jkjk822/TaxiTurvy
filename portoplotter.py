import matplotlib.pyplot as plt
import networkx as nx
import json
from streetMapParser import buildRoadGraph, snapToGraph
from portugalTaxiParser import parseTrips
from collections import defaultdict
from graph import save_graph

graph, edgeTable = buildRoadGraph('portoMap.xml')
print("built")
trips = {}
with open("portoSnappedTrips.json", 'r') as f:
	trips = json.loads(f.read())
print("loaded")
for tripID in trips:
	path = []
	prev = None
	for nodeID in trips[tripID]:
		if prev:
			path += nx.bidirectional_dijkstra(graph, prev, nodeID)[1]
		prev = nodeID
	print(path)
	print(nx.bidirectional_dijkstra(graph, trips[tripID][0], trips[tripID][-1])[1])
	print(nodeID)

nx.draw(graph)
nx.write_gexf(trips, "porto.gexf")
#save_graph(graph,"test.pdf")