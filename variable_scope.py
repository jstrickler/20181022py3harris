#!/usr/bin/env python
import sys

# def print(*args, **kvargs):
#     sys.stdout.write("HA HA HA\n")

x = 100

def spam():
    # x = "folderol"
    print("in spam(): x is", x)
    actor = "Leo"

spam()
print("in main: x is", x)

# local -> nested -> global -> builtin

def outer():
    name = 'Bob'

    def inner():
        print("My name is", name)
        return "Whooooo"

    return inner


f = outer()
result = f()
print(result)

outer.inner()
