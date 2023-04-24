# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import itertools
from string import ascii_uppercase, ascii_lowercase, digits

pattern = (''.join(map(''.join, itertools.product(ascii_uppercase, ascii_lowercase, digits))).encode())[:1000]

# print(pattern)
print("eip:")
print(pattern.find(bytes.fromhex('32714131')[::-1]))
print("esp:")
print(pattern.find(bytes.fromhex('71413471')[::-1]))
print("ebp:")
print(pattern.find(bytes.fromhex('34744133')[::-1]))
