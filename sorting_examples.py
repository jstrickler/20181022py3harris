#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f0 = sorted(fruits)
print("f0:", f0, '\n')

print(str.lower("HELP ME!"))
f1 = sorted(fruits, key=str.lower)
print("f1:", f1, '\n')

def ignore_case(e):
    return e.lower()

f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def custom_sort(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=custom_sort)
print("f4:", f4, '\n')

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}
print(airports.items())

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(element):
    return element[1], element[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()


people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

def by_last_name(person):
    return person[1], person[0]

for first_name, last_name, _ in sorted(people, key=by_last_name):
    print(first_name, last_name)
print('\n')

for first_name, last_name, _ in sorted(people, key=lambda p: (p[1], p[2])):
    print(first_name, last_name)
