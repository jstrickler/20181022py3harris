#!/usr/bin/env python
import typing

def get_message():
    return "Make it warmer!"

m = get_message()

print(m)

get_message()

x = get_message

print(x)

def print_message():
    m = get_message()
    print(m)

print_message()

def spam(x, y):
    return x * y ** y

print(spam(2, 5))
print(spam(7, 19))

# print(spam(7, 8, 9))
print(spam("uh-oh", 3))

def concat(x, y):
    if not isinstance(x, float):
        raise ValueError('parameter x must be a float')
    if not isinstance(y, float):
        raise ValueError('parameter y must be a float')
    return x + y

# print(concat(1.2, 3.4))
# print(concat("foo", "bar"))
# print(concat(5, 10))
# print(concat([1,2,3],[4,5,6]))

def concat2(
        x: typing.Union[int, float],
        y: typing.Union[int, float]
) -> float:
    return int(x + y)

x = concat2('a', 'b')

print(concat.__annotations__)

