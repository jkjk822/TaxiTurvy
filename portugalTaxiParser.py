from streetMapParser import buildRoadGraph, snapToGraph
import networkx as nx

# Windows Linux subsystem workarounds
import matplotlib
matplotlib.use('Agg')
# Windows Linux subsystem workarounds
import matplotlib.pyplot as plt

import json

def parseTrips(filename):
	trips = {}
	with open(filename) as f:
		f.readline()
		for line in f:
			tripID = line.split(",")[0][1:-1] #trim quotes
			rawTripData = line.split("\",\"")[-1][1:-3] #trim outer brackets
			if not rawTripData:
				continue
			rawTripData = rawTripData[1:-1] #trim first and last bracket
			tripData = [(float(pair.split(",")[1]), float(pair.split(",")[0])) for pair in rawTripData.split("],[")]
			trips[tripID] = tripData
	return trips

trips = parseTrips('portoTaxi.csv')
print("parsed trips")
graph, edgeTable = buildRoadGraph('portoMap.xml')
print("graph built")
trips, error = snapToGraph(trips, graph)
print("snapped to graph")
with open("portoSnappedTrips.json", 'w') as f: # encode for later use
	f.write(json.dumps(trips, indent=4))
print("wrote to file")
print(error)

#Read back in using:
# with open("portoSnappedTrips.json", 'r') as f:
# 	print(json.loads(f.read()))


#for u, v, keys, dist in graph.edges(data='dist', keys=True):
#	print(dist)
# nx.draw(graph)
# plt.savefig('test.pdf')