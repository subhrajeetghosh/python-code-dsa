#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# Learning of different string methods & usage of those
name = "subhaa"
print(len(name))  # length of the string
print(name.find("u"))  # case sensitive
print(name.capitalize())  # Capitalize the String
print(name.upper())  # all os the character in the string will be uppercase
print(name.isdigit())  # check whether it is digit value -- here it is false
print(name.isalpha())  # check whether all the character in alphabet
print(name.count("a"))  # check count of a character in the string
print(name.replace("a", "o"))  # replacing chracter in a string
print(name * 5)  # multiply the string by itself

name = "SUBHA"
print(name.lower())  # reverse of above

name = "25"
print(name.isdigit())  # check whether it is digit value -- here it is true

# string slicing
full_name = "John Michel"
print_character = full_name[3]
print(print_character)
first_name = full_name[:4]  # also [0:4] this going to work
print(first_name)
last_name = full_name[5:]  # also [5:11] going to work as we are not mentioning its take upto last value
print(last_name)
funny_name = full_name[0:11:2]  # also you can write this [::2] here you are skiping character by loop
print(funny_name)
reversed_full_name = full_name[::-1]
print(reversed_full_name)  # reversing the string

"""
# Indexing
[] -> this is index operator
Positive indexing starts from the beginning of the sequence and counts up. For example, the first element in a list
has the index 0, the second element has the index 1, and so on.

Negative indexing starts from the end of the sequence and counts down. For example, the last element in a list
has the index -1, the next-to-last element has the index -2, and so on.
"""

website = "https://google.com"

