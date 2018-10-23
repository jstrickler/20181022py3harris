#!/usr/bin/env python

# with EXPR as VAR:
with open('DATA/mary.txt') as mary_in:
    pass


mary_in = open('DATA/mary.txt')
mary_in.close()

# way #1

with open('DATA/mary.txt') as mary_in:
    for line in mary_in:
        print(line, end='')

print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\n\r')
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(len(contents))
    print(repr(contents))
print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    lines = mary_in.readlines()
    print(lines)
print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    lines = [line.rstrip() for line in mary_in]
    print(lines)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines = (line.rstrip() for line in mary_in)
    print(lines)
print('-' * 60)


#  open(FILE_PATH, MODE)
#   MODE    "r"  "w"  "a"   "rb" "wb" "ab"





