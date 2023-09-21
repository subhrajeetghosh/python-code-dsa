#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

"""

A dictionary in Python is a collection of key-value pairs. Keys must be unique, and values can be any type of object,
including other dictionaries. Dictionaries are unordered, meaning that the order in which the key-value pairs are added
to the dictionary is not preserved.
"""

my_dict = {"name": "Alice", "age": 25, "occupation": "Software Engineer"}
print(my_dict['name'])  # if value not present will throw an error for that use get()
print(my_dict.get('company'))  # will print none as the key is not avaialble
print(my_dict.keys())  # print all the keys avaialbe in the dictionary
print(my_dict.values())  # print all the values avaialbe in the dictionary
print(my_dict.items())  # print all the items in dictionary including keys and values

my_dict.update({"name": "Subhaa"})  # update the item
my_dict.pop("age")  # remove item
for key, value in my_dict.items():
    print(key, value)
my_dict.clear()  # clear every data inside dictionary
