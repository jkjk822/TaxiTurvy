from xml.etree import ElementTree as ET
import networkx as nx

tree = ET.parse('map')
root = tree.getroot()


graph = nx.MultiDiGraph()

##############
# Find nodes #
##############
# Each node has the form
#   <node id="1890707217" lat="39.8583920" lon="116.1331899" version="1" timestamp="2012-08-30T22:40:49Z" changeset="12924496" uid="376715" user="R438"/>
# and we hash it with `id` as they key and only keeping the `lat` and `lon` attributes
nodes = {}
for node in root.findall('node'):
	nodes[node.get('id')] = { key: float(node.get(key)) for key in ['lat','lon'] }

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

edges = {}
for way in root.findall('way'):
	highway = False
	for tag in way.findall('tag'):
		if tag.get('k')=='highway':
			highway	= True
			break
	if highway: # Graph construction (see below)
		edgeID = way.get('id')
		edges[edgeID] = {tag.get('k'):tag.get('v') for tag in way.findall('tag')}
		prev = None
		for node in way.findall('nd'):
			nodeID = node.get('ref')
			graph.add_node(nodeID, **nodes[nodeID])
			if prev:
				graph.add_edge(prev, nodeID, key=edgeID)
				if edges[edgeID].get('oneway', 'no') != 'yes':
					graph.add_edge(nodeID, prev, key=edgeID)
			prev = nodeID


##############################
# Graph Construction (above) #
##############################
# We add only the nodes which are part of a highway
#
# We add edges between each of these nodes, only
# directly storing their `id`. We store the rest of
# the meta-data in a separate dict to conserve space.


print(len(graph.nodes))
print(len(edges))
print(len(graph.edges))
print(edges)