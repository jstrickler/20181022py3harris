#!/usr/bin/env python


while True:
    user_name = input("What is your name (or q to quit)? ")
    if user_name == 'q':
        break
    elif user_name == '':
        continue
    else:
        print("Doing user stuff for {}".format(user_name))
