#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

for fruit in fruits:
    print(fruit.upper())
print()

for ch in fruits[8]:
    print(ch)
print()

# for VAR in ITERABLE:
#    ...

print(fruits[0], fruits[1], fruits[-3])
print(fruits, '\n')

print(fruits[0:5])
print(fruits[3:9])
print(fruits[:3])
print(fruits[15:])

fruits[1:4] = ['coconut']
print(fruits)

actor = 'Leonardo DiCaprio'

print(actor[11:14])

print(actor[::2])
print(actor[1::2])





