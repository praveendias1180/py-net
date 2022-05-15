import xml.etree.ElementTree as ET
tag1 = ET.Element('tag1')

tag2 = ET.SubElement(tag1, 'tag2')
tag2.text = 'Animal'

tag3 = ET.SubElement(tag1, 'tag3')
tag3.text = 'Domestic'

tag4 = ET.SubElement(tag1, 'tag4')

tag4p1 = ET.SubElement(tag4, 'tag4.1')
tag4p1.text = 'Cat'

tag4p2 = ET.SubElement(tag4, 'tag4.2')
tag4p2.text = 'Persian'

tag5 = ET.SubElement(tag1, 'tag5')
tag5.text = 'Iran'

tag6 = ET.SubElement(tag1, 'tag6')
tag6.text = 'Male'

tag7 = ET.SubElement(tag1, 'tag7')
tag7.text = '2021.05.04'


print(ET.dump(tag1))