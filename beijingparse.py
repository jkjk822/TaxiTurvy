# Mo Ahmed beijingparse.py

from xml.etree import ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
import numpy as np

np.set_printoptions(threshold=np.nan)


def parseTrips(start,end):
	# Initialize empty array
	full = []
	taxiID = []
	datetime = []
	longi = []
	lat = []

	# Loop through all Beijing Taxi .txt files line by line and pull info, number of .txt files hardcoded in for now
	for i in range(start,end):
		with open (str(i)+'.txt') as text:
			text.readline()
			for line in text:
				#if longi[line] != 0 and lat[line] != 0:
				full.append(line.strip().split(","))
				taxiID.append(line.strip().split(",")[0])
				datetime.append(line.strip().split(",")[1])
				longi.append(line.strip().split(",")[2])
				lat.append(line.strip().split(",")[3])

	# Turn all arrays in numpy arays
	full = np.array(full)
	taxiID = np.array(taxiID)
	datetime = np.array(datetime)
	longi = np.array(longi)
	lat = np.array(lat)

	# Coordinate matrix (longtiude, latitude)
	coord = np.column_stack((longi,lat))

	# Trip matrix (taxiID, longtiude, latitude)
	trips = np.column_stack((taxiID,coord))

	# Create position dict
	pos = {}
	for i in range(0,len(coord)):
		pos.update({i:(coord[i,0],coord[i,1])})

	#print(trips)

	# Return info
	return (pos)

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


