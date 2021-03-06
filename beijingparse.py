# Mo Ahmed beijingparse.py

from xml.etree import ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
import numpy as np

np.set_printoptions(threshold=np.nan)


def parseTrips(start,end):
	# Initialize empty array
	#full = []
	#taxiID = []
	#datetime = []
	longi = []
	lat = []

	# Loop through all Beijing Taxi .txt files line by line and pull info, number of .txt files hardcoded in for now
	#for i in range(start,end):
	#	with open (str(i)+'.txt') as text:
	#		text.readline()
	#		for line in text:
	#			full.append(line.strip().split(","))
	#			taxiID.append(line.strip().split(",")[0])
	#			datetime.append(line.strip().split(",")[1])
	#			longi.append(line.strip().split(",")[2])
	#			lat.append(line.strip().split(",")[3])

	# Turn all arrays in numpy arays
	#full = np.array(full)
	#taxiID = np.array(taxiID)
	#datetime = np.array(datetime)
	#longi = np.array(longi)
	#lat = np.array(lat)

	# Coordinate matrix (longtiude, latitude)
	#coord = np.column_stack((longi,lat))

	# Trip matrix (taxiID, longtiude, latitude)
	#trips = np.column_stack((taxiID,coord))

	#print(trips)

	pos = {}

	for i in range(start,end):
		with open (str(i)+'.txt') as text:
			text.readline()
			xy = []
			for line in text:
				xy.append((line.strip().split(",")[2],line.strip().split(",")[3]))
				longi.append(line.strip().split(",")[2])
				lat.append(line.strip().split(",")[3])
			pos.update({str(i):xy})

	longi = np.array(longi)
	lat = np.array(lat)
	coord = np.column_stack((longi,lat))

	# Create graph dict
	vis = {}
	for i in range(0,len(coord)):
		vis.update({i:(coord[i,0],coord[i,1])})

	# Return info
	return pos
	#return vis

##############
# Merge nodes with map data


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


