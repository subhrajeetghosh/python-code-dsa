#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

name = input("hello write: ")
print("hello " + name)

# when we accept input from user its always in String datatype

age = input("write your age: ")
age += 1  # this will give you error as now the age is String type for testing comment it out

age = int(input("write your age: "))  # doing type casting for getting it in integer form
age += 1
print(age)
