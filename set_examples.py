#!/usr/bin/env python

letters = "a b c".split()

john_countries = """Canada
Mexico
Barbados
China
UK
Austria
Spain
Bulgaria
Israel""".split()

clare_countries = """BVI
Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".split()

john = set(john_countries)
clare = set(clare_countries)


print("john:", john, '\n')
print("clare:", clare, '\n')

print("both:", john & clare)
print("either:", john | clare)
print("just one:", john ^ clare)
print("just Clare:", clare - john)
print("just John:", john - clare)








