#!/usr/bin/env python

# import xml.etree.ElementTree as ET
import lxml.etree as ET

doc = ET.parse('DATA/solar.xml') # <1>

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print('\t' + moon.text)
