

trips = {}
with open('portugalTaxi.csv') as f:
	f.readline()
	for line in f:
		tripID = line.split(",")[0][1:-1] #trim quotes
		rawTripData = line.split("\",\"")[-1][1:-3] #trim outer brackets
		if not rawTripData:
			continue
		rawTripData = rawTripData[1:-1] #trim first and last bracket
		tripData = [(float(pair.split(",")[0]), float(pair.split(",")[1])) for pair in rawTripData.split("],[")]
		trips[tripID] = tripData

print(len(trips))