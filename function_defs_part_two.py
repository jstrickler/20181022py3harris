#!/usr/bin/env python

def doit(a, b):
    print(a, b)

def hello(greeting, *greetee):
    for person in greetee:
        print(f"{greeting}, {person}")

hello("Hi", 'world')
hello("Hello", 'lady')
hello("good morning", 'bedbug')
print()
hello("Hey", 'Zac', 'Cindy', 'Jane', 'Elsie', 'Jeff')
hello("a", "b", "c")

def hi(greetee="world"):
    print("Hello,", greetee)

hi("Mom")
hi()

def spam(a, b, *others):
    print(a, b)
    print(others)

spam("wombat", "wallaby")

spam("wombat", "wallaby", 'Kangaroo', 'fruitbat')

spam("wombat", "wallaby", 'Kangaroo', 'fruitbat', 'crocodile')

def doit(*, file_name, user_name="NONE"):
    print("file_name:", file_name)
    print("user_name:", user_name)

doit(file_name='foo.txt', user_name='bob')
doit(user_name='fred', file_name='spam.txt')
doit(file_name='raccoon.txt')

def config(**values):
    for k, v in values.items():
        print(k, v)

config(actor='Leo DiCaprio', movie="What's Eating Gilbert Grape", rating=8.9)

