#!/usr/bin/env python

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[0]
        if first_letter in letter_counts:
            # letter_counts[first_letter] = letter_counts[first_letter] + 1
            letter_counts[first_letter] += 1
        else:
            letter_counts[first_letter] = 1

for letter, count in sorted(letter_counts.items()):
    print(letter, count)
print('*' * 60)

def by_value(kvpair):
    return kvpair[1], kvpair[0]

for letter, count in sorted(letter_counts.items(), key=by_value,
                            reverse=True):
    print(letter, count)
print('*' * 60)

