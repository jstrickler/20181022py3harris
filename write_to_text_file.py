#!/usr/bin/env python

fl_info = [
    ('Palm Bay', 'Brevard'),
    ('Melbourne', 'Brevard'),
    ('Jacksonville', 'Duval'),
    ('Miami', 'Dade'),
    ('Orlando', 'Orange'),
    ('Kissimmee', 'Osceola'),
]

with open('florida_cities.txt', 'w') as fl_cities_out:
    for info in fl_info:
        record = '\t'.join(info) + '\n'
        fl_cities_out.write(record)


with open('florida_cities.txt', 'w') as fl_cities_out:
    for city, county in fl_info:
        record = f"{city}\t{county}\n"
        fl_cities_out.write(record)
