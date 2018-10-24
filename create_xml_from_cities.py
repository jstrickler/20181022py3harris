#!/usr/bin/env python
import lxml.etree as ET

fl_info = [
    ('Palm Bay', 'Brevard'),
    ('Melbourne', 'Brevard'),
    ('Jacksonville', 'Duval'),
    ('Miami', 'Dade'),
    ('Orlando', 'Orange'),
    ('Kissimmee', 'Osceola'),
]

cities = ET.Element('cities')
for city_name, county in fl_info:
    city = ET.SubElement(cities, 'city', county=county)
    city_name_element = ET.SubElement(city, 'cityname')
    city_name_element.text = city_name
    pop = ET.SubElement(city, 'population')
    pop.text = "1234"

print(ET.tostring(cities, pretty_print=True).decode())

doc = ET.ElementTree(cities)
doc.write('fl_cities.xml', pretty_print=True, xml_declaration=True)
