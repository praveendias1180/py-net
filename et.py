import xml.etree.ElementTree as ET
tree = ET.parse('vehicle.xml')
root = tree.getroot()

print(tree)
print(root)

for child in root:
    print(child.tag, child.attrib)

print(root[1][1].text)