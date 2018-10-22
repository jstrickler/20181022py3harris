#!/usr/bin/env python

person = "Robert", "Smith", 47, 'FL'


print(person[0], person[1], person[2])


first_name, last_name, *stuff = person

print(last_name, stuff)


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)
