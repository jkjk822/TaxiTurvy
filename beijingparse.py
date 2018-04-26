# Mo Ahmed beijingparse.py

from xml.etree import ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(threshold=np.nan)

# Initialize empty array
full = []
taxiID = []
datetime = []
longi = []
lat = []

# Loop through all Beijing Taxi .txt files line by line and pull info, number of .txt files hardcoded in for now
for i in range(1,10358):
	with open (str(i)+'.txt') as text:
		text.readline()
		for line in text:
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
print(trips)

##############
# Merge nodes with map data


##############
# Plot each coordinate as a node in NetworkX, this looks really messy right now and will need to be updated

G = nx.MultiDiGraph()
pos = {}

# Create position dict
for i in range(0,len(coord)):
	pos.update({i:(coord[i,0],coord[i,1])})

# Add nodes from dict
G.add_nodes_from(pos.keys())
#G.add_edges_from([(0,1), (1,2), (2,3)])

# Draw and plot
nx.draw(G, pos, with_labels=True)
plt.show()
