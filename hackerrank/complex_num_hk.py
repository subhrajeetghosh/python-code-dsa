#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh


from cmath import *
from math import *
m1 = complex(input())

# Extract real and imaginary parts
x = m1.real
y = m1.imag


print(sqrt(x*x + y*y))
print(phase(complex(x, y)))
