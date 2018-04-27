from xml.etree import ElementTree as ET
import networkx as nx
import scipy
import numpy as np

def buildRoadGraph(filename):
	return __linkNodes(ET.parse(filename).getroot())

#################
# Find highways #
#################
# Each line is represented by a `way` having the form
#	<way id="390165664" version="1" timestamp="2016-01-08T02:58:18Z" changeset="36437578" uid="288524" user="Chen Jia">
#		<nd ref="3933265004"/>
#		... (more nd elements)
#		<tag k="highway" v="service"/>
#	</way>
# and we only consider it if it has k="highway".
# We only keep the `id` from the way tag itself.
#
# The `highway` key has the type of the road as its value
# Other key-value pairs include additional information such as
# oneway, etc.
# We keep all this information for future use

def __linkNodes(root):
	graph = nx.MultiDiGraph()
	nodes = __findNodes(root)

	edges = {}
	noCars = ['footway','cycleway','path']
	for way in root.findall('way'):
		highway = False
		for tag in way.findall('tag'):
			if tag.get('k')=='highway' and tag.get('v') not in noCars:
				highway	= True
				break
		if highway:
			__addToGraph(way, nodes, edges, graph)
	return (graph, edges)


##############
# Find nodes #
##############
# Each node has the form
#   <node id="1890707217" lat="39.8583920" lon="116.1331899" version="1" timestamp="2012-08-30T22:40:49Z" changeset="12924496" uid="376715" user="R438"/>
# and we hash it with `id` as the key and only keeping the `lat` and `lon` attributes
def __findNodes(root):
	nodes = {}
	for node in root.findall('node'):
		nodes[node.get('id')] = { "loc": (float(node.get('lat')), float(node.get('lon'))) }
	return nodes


######################
# Graph Construction #
######################
# We add only the nodes which are part of a highway
#
# We add edges between each of these nodes, only
# directly storing their `id`. We store the rest of
# the meta-data in a separate dict to conserve space.

def __addToGraph(way, nodes, edges, graph):
	edgeID = way.get('id')
	edges[edgeID] = {tag.get('k'):tag.get('v') for tag in way.findall('tag')}
	prevID = None
	for node in way.findall('nd'):
		nodeID = node.get('ref')
		graph.add_node(nodeID, **nodes[nodeID])
		if prevID:
			dist = __distance(nodes[prevID]['loc'], nodes[nodeID]['loc'])
			graph.add_edge(prevID, nodeID, key=edgeID, dist=dist)
			if edges[edgeID].get('oneway', 'no') != 'yes':
				graph.add_edge(nodeID, prevID, key=edgeID, dist=dist)
		prevID = nodeID


# Distance formula (we should proably use haversine here)
def __distance(p1, p2):
	return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2


# This is super computationally expensive, so watch out
def snapToGraph(trips, graph):
	snappedTrips = {}
	nodeIDs = np.array([x[0] for x in graph.nodes.data('loc')])
	NNTree = scipy.spatial.cKDTree(np.array([x[1] for x in graph.nodes.data('loc')]))
	error = 0
	for tripID in trips:
		# find 1 nearest neighbor for each trip point
		dists, indexes = NNTree.query(trips[tripID], k=1, n_jobs=-1)
		error += dists.sum()
		snappedTrips[tripID] = []
		for i in indexes:
			snappedTrips[tripID].append(nodeIDs[i])
	return (snappedTrips, error)