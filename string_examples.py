#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'''spam\n'''

print("It's all good")

print('The "fix" is in"')

print("""It's all about the "good" and the "bad" (and maybe the "ugly")""")

sql_snippet = """
select *
from customers
where last_name = "Morris"
"""
