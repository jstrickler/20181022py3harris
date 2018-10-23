#!/usr/bin/env python
from collections import Counter


with open('DATA/words.txt') as words_in:
    counts = Counter((word[0] for word in words_in))

print(counts.most_common())

