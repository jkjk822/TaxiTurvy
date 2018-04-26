# Mo Ahmed portoparse.py

from xml.etree import ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(threshold=np.nan)

# Initialize empty array
full = []
tripID = []
calltype = []
origincall = []
originstand = []
taxiID = []
timestamp = []
daytype = []
missingdata = []
longi = []
lat = []


# Loop through all Porto Taxi .txt files line by line and pull info, number of .txt files hardcoded in for now
with open ('SamplePorto.txt') as text:
	text.readline()
	for line in text:
		full.append(line.strip().split(","))
		tripID.append(line.strip().split(",")[0])
		calltype.append(line.strip().split(",")[1])
		origincall.append(line.strip().split(",")[2])
		originstand.append(line.strip().split(",")[3])
		taxiID.append(line.strip().split(",")[4])
		timestamp.append(line.strip().split(",")[5])
		daytype.append(line.strip().split(",")[6])
		missingdata.append(line.strip().split(",")[7])
		for i in range(8,len(line.strip().split(",")),2):
			longi.append(line.strip().split(",")[i])
			lat.append(line.strip().split(",")[i+1])

# Turn all arrays in numpy arays
full = np.array(full)
tripID = np.array(tripID)
calltype = np.array(calltype)
origincall = np.array(origincall)
originstand = np.array(originstand)
taxiID = np.array(taxiID)
timestamp = np.array(timestamp)
daytype = np.array(daytype)
missingdata = np.array(missingdata)
longi = np.array(longi)
lat = np.array(lat)

# Coordinate matrix (longtiude, latitude), work in progress need to remove extra brackets
coord = np.column_stack((longi,lat))
print(coord)

# The rest is work in progress

# Trip matrix (taxiID, longtiude, latitude)
#trips = np.column_stack((taxiID,coord))


##############
# Plot each coordinate as a node in NetworkX

#G = nx.MultiDiGraph()
#pos = {}

# Create position dict
#for i in range(0,len(coord)):
#	pos.update({i:(coord[i,0],coord[i,1])})

# Add nodes from dict
#G.add_nodes_from(pos.keys())
#G.add_edges_from([(0,1), (1,2), (2,3)])

# Draw and plot
#nx.draw(G, pos, with_labels=True)
#plt.show()
