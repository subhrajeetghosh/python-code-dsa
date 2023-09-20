#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# for loop is a statement that will execute a block of code a limited amount of times only if condition met

# Generate a sequence of numbers from 0 to 4
range(5)

# Generate a sequence of numbers from 2 to 6, inclusive
range(2, 7)

# Generate a sequence of numbers from 1 to 10, incrementing by 2
range(1, 11, 2)

# Generate a sequence of numbers from 10 to 1, incrementing by 1
range(10, 0, -1)

for i in range(10, 0, -1):
    print(i)

# printing character throgh for loop
for i in "Subhaa":
    print(i)

# while loop :programming construct allows you to execute a block of code repeatedly as long as a condition is true
name = ""

while name != "test":
    print("write your correct name")
    name = input()

# Nested loop is a loop inside another loop.
# This means that the inner loop will be executed for each iteration of the outer loop.

rows = int(input("enter the number of rows you want? : "))
column = int(input("enter the number of columns you want? : "))
symbol = input("enter the symbol you want to print : ")
for i in range(rows):
    for j in range(column):
        print(symbol, end=" ")  # end will help up keep printing in the same line with one space each time
    print()
