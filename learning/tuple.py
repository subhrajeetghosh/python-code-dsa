#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

"""
A tuple in Python is an immutable sequence of objects. This means that a tuple cannot be changed once it is created.
Tuples are written using parentheses (), and the elements of a tuple are separated by commas.
"""

tuplee = ("subhaa", 25, "male")
print(tuplee.count("subhaa"))  # no of times that elements appered in the tople
print(tuplee.index(25))  # index of the element

for x in tuplee:
    print(x)

if 25 in tuplee:
    print("25 exist")
