from xml.etree import ElementTree as ET

tree = ET.parse('map')
print(len(tree.findall('way')))
root = tree.getroot()

roads = []
for way in root.findall('way'):
	highway = False
	for tag in way.findall('tag'):
		if tag.get("k")=='highway':
			highway	= True
			break
	if highway:
		roads.append(way)
		for 

print(len(roads))