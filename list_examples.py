#!/usr/bin/env python

list1 = list()
presidents = ['Lincoln', 'Ford', 'Tyler', 'Van Buren']
print(presidents[0], presidents[3])

list2 = []
colors = 'red green purple grey chartreuse'.split()

print(list1)
print(list2)
print(presidents)
print(colors)

presidents.append('Roosevelt (Teddy)')

presidents.append('Washington')

print(presidents)

presidents.insert(0, 'Nixon')
presidents.insert(5, 'McKinley')

print(presidents)

more_potus = ['Truman', 'Grant', 'Taft']

presidents.extend(more_potus)

print(presidents)

print(presidents[0], presidents[3], presidents[-1], presidents[len(presidents) - 1])


del presidents[4]

print(presidents)

presidents.remove('Nixon')

print(presidents)

p = presidents.pop()
print(p)
print(presidents)

p = presidents.pop(3)
print(p)
print(presidents)















