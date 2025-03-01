import numpy as np
import numpy.linalg as la

np.random.seed(123)

A = np.array([
    [1, 4],
    [4.5, 4],
    [3, 5]
])

b = np.array([2.5, 5, 4])

x = np.zeros(A.shape[1])

grad = 2 * A.T @ (A @ x - b)

L = 2 * la.norm(A.T @ A, 2)

epsilon = 1e-5

while np.linalg.norm(grad) > epsilon:
    alpha = 1 / L
    x = x - alpha * grad
    grad = 2 * A.T @ (A @ x - b)

delightfulbite_cafe = np.array([3, 3])
sarah_rating = delightfulbite_cafe @ x

print("Vector x:", x)
print("Estimated rating for DelightfulBite Cafe:", sarah_rating)
print("Norm of the gradient: {:.5f}".format(la.norm(grad)))
