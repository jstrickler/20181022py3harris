#!/usr/bin/env python
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

print(d6.setdefault(test_color, -1))
print(d6, '\n')

more_colors = {'chartreuse': 6, 'navy': 9,
               'charcoal grey': 2, 'blue': 1}

d6.update(more_colors)
print(d6, '\n')

print(d6.keys())
print(d6.values())

print('green' in d6)
print('forest green' in d6)
print(len(d6))

for color, color_value in d6.items():
    print(color, color_value)
print()

print(d6.items(), '\n')


for color, color_value in sorted(d6.items()):
    print(f"{color:14s} {color_value:3d}")
print()


