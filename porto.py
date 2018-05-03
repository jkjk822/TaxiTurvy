# Windows Linux subsystem workarounds
import matplotlib
matplotlib.use('Agg')
# Windows Linux subsystem workarounds
import matplotlib.pyplot as plt
import networkx as nx
import json
from streetMapParser import buildRoadGraph, snapToGraph
from portugalTaxiParser import parseTrips
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
graph, edgeTable = buildRoadGraph('portoMap.xml')
print("built")
trips = {}
with open("portoSnappedTrips.json", 'r') as f:
	trips = json.loads(f.read())
print("loaded")
with open('expandedPaths.json', 'a') as f:
	complete = ['1379604446620000574', '1388548028620000074', '1391760659620000010', '1375724022620000663', '1399572669620000506',
	'1395130170620000024', '1395937013620000007', '1383449835620000472', '1384692749620000126', '1393958970620000648',
	'1403853551620000286', '1378489645620000391', '1391779432620000074', '1399820029620000686', '1380375278620000383',
	'1395655073620000480', '1403478070620000453', '1379712261620000904', '1392633621620000036', '1387654944620000465', 
	'1379661410620000195', '1378976826620000353', '1397989762620000565', '1379609130620000605', '1378796683620000389', 
	'1379781166620000343', '1387531512620000294']
	done = len(complete)
	for tripID in trips:
		if(tripID in complete):
			continue
		path = []
		trip = trips[tripID]
		for i in range(len(trip)):
			if i>0:
				valid = False
				nextSteps = []
				j = i
				while(not valid and i < len(trip)):
					try:
						d, nextSteps = nx.bidirectional_dijkstra(graph, trip[j-1], trip[i])
						valid = True
						if len(nextSteps)>10 and i+1 < len(trip):
							d, nextNext = nx.bidirectional_dijkstra(graph, trip[j-1], trip[i+1])
							if len(nextNext) < len(nextSteps):
								nextSteps = nextNext
								i+=1
					except nx.exception.NetworkXNoPath:
						i+=1
				path += nextSteps
		path = [n for i, n in enumerate(path) if i==0 or n != path[i-1]] #remove dupes
		if len(path)<2:
			continue
		f.write(tripID+"\n")
		f.write(json.dumps(path)+"\n")
		f.write(json.dumps(nx.bidirectional_dijkstra(graph, path[0], path[-1])[1])+"\n")
		f.write("\n")
		done+=1
		print(done)


##################
# For resnapping #
##################
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

