#!/usr/bin/env python

import lxml.etree as ET

doc = ET.parse('DATA/presidents.xml')

root = doc.getroot()
print(root)

# president_list = doc.find('.//presidents')

for president in doc.findall('.//president'):
    first_name = president.find('name/first').text
    last_name = president.find('name/last').text
    birth_state = president.find('birthstate').text
    print(f'{first_name:28s} {last_name:20s} {birth_state}')
