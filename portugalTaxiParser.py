from streetMapParser import buildRoadGraph

def parseTrips(filename):
	trips = {}
	with open(filename) as f:
		f.readline()
		for line in f:
			tripID = line.split(",")[0][1:-1] #trim quotes
			rawTripData = line.split("\",\"")[-1][1:-3] #trim outer brackets
			if not rawTripData:
				break
			rawTripData = rawTripData[1:-1] #trim first and last bracket
			tripData = [(float(pair.split(",")[0]), float(pair.split(",")[1])) for pair in rawTripData.split("],[")]
			trips[tripID] = tripData
	return trips


trips = parseTrips('portoTaxi.csv')
graph, edgeTable = buildRoadGraph('portoMap.xml')