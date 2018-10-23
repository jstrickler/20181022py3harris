#!/usr/bin/env python
from collections import defaultdict

d1 = dict()
d2 = {'red': 5, 'green': 10, 'orange': 3}
d3 = {}

d4 = dict(red=5, green=10, orange=3)

pairs = [
    ('red', 5),
    ('green', 10),
    ('orange', 3),
]

d5 = dict(pairs)

colors = 'red green orange'.split()
values = [5, 10, 3]

d6 = dict(zip(colors, values))

print(list(zip(colors, values)))

d6['blue'] = 8
print(d6, '\n')

d6['pink'] = 3
d6['scarlet'] = 3

print(d6)

d6['scarlet'] = 7

print(d6)

del d6['pink']
print(d6)

print(d6['green'], '\n')

for k in ['green', 'blue', 'red']:
    print(d6[k])
print()

test_color = 'purple'
if test_color in d6:
    print(d6[test_color])

print(d6.get(test_color))
print(d6.get(test_color, -1))

defd = defaultdict(list)

print(defd['foo'])
defd['foo'].append('A')
defd['foo'].append('B')
defd['bar'].append('C')

print(defd, '\n')

words_by_letter = defaultdict(list)
with open('DATA/alt.txt') as alt_in:
    for raw_line in alt_in:
        word = raw_line.rstrip()
        first_letter = word[0]
        words_by_letter[first_letter].append(word)

print(words_by_letter)
