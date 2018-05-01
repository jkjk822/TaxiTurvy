# Windows Linux subsystem workarounds
import matplotlib
matplotlib.use('Agg')
# Windows Linux subsystem workarounds
import matplotlib.pyplot as plt
import networkx as nx
import json
from streetMapParser import buildRoadGraph, snapToGraph
from beijingparse import parseTrips
from collections import defaultdict



# totalTypes = defaultdict(int)
# i=0;
# for c in nx.weakly_connected_components(graph):
# 	g = graph.subgraph(c)
# 	nx.draw_networkx(g, {x:y[::-1] for x,y in g.nodes.data('loc')}, node_size=3, width=.1, arrowsize=2, with_labels=False, alpha=.7)
# 	plt.ticklabel_format(useOffset=False)
# 	plt.savefig(str(i)+"test.pdf")
# 	i+=1
# 	types = defaultdict(int)
# 	for x in graph.subgraph(c).edges:
# 		types[edgeTable[x[2]]['highway']] += 1
# 		if edgeTable[x[2]]['highway']=='residential':
# 			print(graph.nodes[x[1]]['loc'])
# 	print(i)
# 	print(types)
# 	for k in types:
# 		totalTypes[k] += types[k]
# print(totalTypes)

#######################
#Read in trips using: #
#######################
# graph, edgeTable = buildRoadGraph('beijingMap.xml')
# print("built")
# trips = {}
# with open("beijingSnappedTrips.json", 'r') as f:
# 	trips = json.loads(f.read())
# print("loaded")
# for tripID in trips:
# 	path = []
# 	prev = None
# 	for nodeID in trips[tripID]:
# 		if prev:
# 			path += nx.bidirectional_dijkstra(graph, prev, nodeID)[1]
# 		prev = nodeID
# 	print(path)
# 	print(nx.bidirectional_dijkstra(graph, trips[tripID][0], trips[tripID][-1])[1])
# 	print()



##################
# For resnapping #
##################
trips = parseTrips(1,5)
print("parsed")
graph, edgeTable = buildRoadGraph('beijingMap.xml')
print("built")
trips, error = snapToGraph(trips, graph)
print("snapped")
with open("beijingSnappedTrips.json", 'w') as f: # encode for later use
	f.write(json.dumps(trips, indent=4))
print("wrote to file")
print(error)




#for u, v, keys, dist in graph.edges(data='dist', keys=True):
#	print(dist)
# nx.draw(graph)
# plt.savefig('test.pdf')

