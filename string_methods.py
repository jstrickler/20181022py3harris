#!/usr/bin/env python


actor = "Leonardo DiCaprio"

print(actor)

print(actor.upper())

print(actor.count('d'))

print(actor.count('Cap'))
print(actor.lower().count('d'))

print(len(actor))

print(actor.startswith('Leo'))
print(actor.startswith('Robert'))

print("Cap" in actor)

print("Hat" in actor)

print(actor.find("Cap"))
print(actor.index("Cap"))

print(actor.find("Hat"))

# print(actor.index("Hat"))

s = "      All my exes live in Texas       "

print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()


s = "xyxxyyxxxyyyAll my exes live in Texasyxyyyyyyyxxxxxxxxx"

print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()

print(s.replace('x', '_').replace('y', '+'))
print(s.replace('x', ''))

print(s.replace('Texas', 'North Carolina'))








