from xml.etree import ElementTree as ET
import networkx as nx
import scipy
import numpy as np

def buildRoadGraph(filename):
	speeds = {}
	if filename.startswith('port'):
		# median speeds
		speeds = {'living_street': 50, 'primary_link': 50, 'primary': 50, 'track': 35, 'unclassified': 50,
		'tertiary_link': 50, 'residential': 50, 'secondary': 50, 'trunk': 120, 'tertiary': 50,
		'service': 30, 'motorway': 100, 'motorway_link': 60, 'secondary_link': 50,
		# inferred
		'road': 50, 'trunk_link': 60}
	elif filename.startswith('beijing'):
		# median speeds
		speeds = {'secondary': 60, 'unclassified': 20,  'living_street': 25, 'primary': 60, 'service': 5,
		'residential': 20, 'primary_link': 20, 'tertiary': 40, 'trunk': 80, 'motorway': 120, 'trunk_link': 40,
		'motorway_link': 60,
		# inferred
		'road': 20, 'access_ramp': 40, 'track': 20, 'tertiary_link': 30, 'secondary_link': 50}
	graph, edgeTable = __linkNodes(ET.parse(filename).getroot(), speeds)
	return (graph.subgraph(max(nx.weakly_connected_components(graph), key=len)), edgeTable)

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

def __linkNodes(root, speeds):
	graph = nx.MultiDiGraph()
	nodes = __findNodes(root)

	edges = {}
	invalid = ['footway','cycleway','path', 'steps', 'construction', 'raceway',
	'proposed', 'planned', 'bridleway', 'bus_stop', 'elevator', 'services',
	'platform','disused', 'no', 'rest_area', 'crossing', 'pedestrian']
	for way in root.findall('way'):
		highway = False
		for tag in way.findall('tag'):
			if tag.get('k')=='highway' and tag.get('v') not in invalid:
				highway	= True
		if highway:
			__addToGraph(way, nodes, edges, speeds, graph)
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
		nodes[node.get('id')] = { "loc": {0:float(node.get('lat')), 1:float(node.get('lon'))} }
	return nodes


######################
# Graph Construction #
######################
# We add only the nodes which are part of a highway
#
# We add edges between each of these nodes, only
# directly storing their `id`. We store the rest of
# the meta-data in a separate dict to conserve space.

def __addToGraph(way, nodes, edges, speeds, graph):
	edgeID = way.get('id')
	edges[edgeID] = {tag.get('k'):tag.get('v') for tag in way.findall('tag')}
	prevID = None
	speed = speeds[edges[edgeID]['highway']]
	if 'maxspeed' in edges[edgeID]:
		speed = int(edges[edgeID]['maxspeed'])
	elif 'maxspeed:lanes' in edges[edgeID]:
		speed = int(edges[edgeID]['maxspeed:lanes'].split('|')[0])
	edges[edgeID]['speed'] = speed
	for node in way.findall('nd'):
		nodeID = node.get('ref')
		graph.add_node(nodeID, **nodes[nodeID])
		if prevID:
			dist = __distance(nodes[prevID]['loc'], nodes[nodeID]['loc'])
			weight = dist/speed
			graph.add_edge(prevID, nodeID, key=edgeID, dist=dist, weight=weight)
			if edges[edgeID].get('oneway', 'no') != 'yes':
				graph.add_edge(nodeID, prevID, key=edgeID, dist=dist, weight=weight)
		prevID = nodeID


# Haversine
def __distance(p1, p2):
	a = np.sin((p1[0]-p2[0])/2)**2+np.cos(p1[0])*np.cos(p2[0])*np.sin((p1[1]-p2[1])/2)**2
	return float(2*6371*np.arctan((a/(1-a))**1/2))


# This is super computationally expensive, so watch out
def snapToGraph(trips, graph):
	snappedTrips = {}
	nodeIDs = np.array([x[0] for x in graph.nodes.data('loc')])
	NNTree = scipy.spatial.cKDTree(np.array([x[1] for x in graph.nodes.data('loc')]))
	maxError = 0
	for tripID in trips:
		# find 1 nearest neighbor for each trip point
		dists, indexes = NNTree.query(trips[tripID], k=1, n_jobs=-1)
		maxError = max(max(dists), maxError)
		snappedTrips[tripID] = []
		j = -1
		for i in indexes:
			if j!=i: #skip duplicates
				snappedTrips[tripID].append(nodeIDs[i])
			j = i
	return (snappedTrips, maxError)