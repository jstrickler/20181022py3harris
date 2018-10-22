#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(min(nums), max(nums), len(nums))
print(sorted(nums))
print(sum(nums))

colors = ['aqua', 'lime', 'coral', 'sable']

print(min(colors), max(colors), len(colors))
print(sorted(colors), '\n')

i = 0
for color in colors:
    print(i, color)
    i += 1
print()

print(list(enumerate(colors)), '\n')

for i, color in enumerate(colors):
    print(i, color.upper())
print()

for i, color in enumerate(colors, 1):
    print(i, color.upper())
print()


for i, ch in enumerate("Harris"):
    print(i, ch)
print()


print('aqua' in colors)
print('arr' in "Harris")

print('hamster' * 10)

flags = [True] * 25

print(flags)

a = ['Melbourne']
b = ['Florida']
c = a + b
print(c)

for i in range(10):
    print("Wombat!")
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')

for i in range(1, 11):
    print(f"{i:02d}")
