import numpy as np

# Example array
y = np.array([1, 0, 1, 1, 0, 0, 1])

# Calculate the proportion of 1's
p1 = len(y[y == 1]) / len(y)

print(len(y[y == 1]))