import numpy as np

rng = np.random.default_rng(123)
n = 10
R = rng.random((n, n))
A = R.T @ R
b = rng.random(n)

def f(x):
    return x @ A @ x + 2.0 * b @ x

def grad_f(x):
    return 2.0 * (A @ x) + 2.0 * b

def project_onto_sum_ge_neg10(x):
    s = np.sum(x)
    if s < -10:
        offset = (-10 - s) / len(x)
        return x + offset
    return x


L = 2.0 * np.linalg.norm(A, 2)
alpha = 1.0 / L

x = np.zeros(n)
tol = 1e-3
max_iter = 10000

for _ in range(max_iter):
    x_new = x - alpha * grad_f(x)
    x_new = project_onto_sum_ge_neg10(x_new)
    
    if np.linalg.norm(x_new - x) < tol:
        x = x_new
        break
    
    x = x_new

print("Solution x =", x)
print("Function value at solution =", f(x))