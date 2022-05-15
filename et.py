import xml.etree.ElementTree as ET
tree = ET.parse('vehicle.xml')
root = tree.getroot()

print(tree)
print(root)