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
