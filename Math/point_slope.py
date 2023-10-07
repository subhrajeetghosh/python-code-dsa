#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

# point Slope formula
x, y = map(int, input("Enter values for x and y separated by a space: ").split())
p, q = map(int, input("Enter values for P and Q separated by a space: ").split())
m = input("Enter value of M: ")

if (y-q) == int(m * (x-p)):
    print("Yes")
else:
    print("No")
