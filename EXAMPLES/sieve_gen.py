#!/usr/bin/env python

def next_prime(limit):
    flags = [False] * (limit+1)  #  <1>

    for i in range(2,limit):
        if flags[i]:
            continue
        for j in range(2*i,limit+1,i):
            flags[j] = True
        yield i  # <2>

for p in next_prime(200):  # <3>
    print(p, end=' ')

