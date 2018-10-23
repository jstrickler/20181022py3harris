#!/usr/bin/env python
from collections import defaultdict

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
