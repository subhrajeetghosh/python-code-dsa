import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import time

np.random.seed(123)
data = scipy.io.loadmat('mushrooms.mat')
A = data['A']
b = data['b'].reshape(-1)
n, m = A.shape
lam = 1e-5

L = 0
for i in range(n):
    ai = A[i, :].toarray().flatten()
    L = np.maximum(L, np.linalg.norm(ai))
L = (L ** 2) / 4

epsilon = 1 / (3 * L)

x = np.zeros(m)


def prox_l1(v, lam):
    return np.sign(v) * np.maximum(np.abs(v) - lam, 0.0)


norm_diffs = []
outer_iters = 10
inner_iters = n

start_time = time.time()

for outer in range(outer_iters):
    x_old_outer = x.copy()

    full_grad = np.zeros(m)
    for i in range(n):
        ai = A[i, :].toarray().flatten()
        bi = b[i]
        s = bi * ai.dot(x)
        grad_i = -bi * ai / (1 + np.exp(s))
        full_grad += grad_i
    full_grad /= n

    x_snapshot = x.copy()

    for inner in range(inner_iters):
        i = np.random.randint(0, n)
        ai = A[i, :].toarray().flatten()
        bi = b[i]

        s_current = bi * ai.dot(x)
        grad_current = -bi * ai / (1 + np.exp(s_current))

        s_snapshot = bi * ai.dot(x_snapshot)
        grad_snapshot = -bi * ai / (1 + np.exp(s_snapshot))

        grad = grad_current - grad_snapshot + full_grad

        x = x - epsilon * grad

        x = prox_l1(x, epsilon * lam)

    diff_norm = np.linalg.norm(x - x_old_outer) / epsilon
    norm_diffs.append(diff_norm)

running_time = time.time() - start_time
print(f"Running time for Proximal SVRG++: {running_time:.2f} seconds")

plt.figure(figsize=(8, 6))
plt.plot(range(1, outer_iters + 1), norm_diffs, marker='o')
plt.xlabel('Epoch (Outer Iterations)')
plt.ylabel(r'$\|x_k - x_{k-1}\| / \epsilon$')
plt.title('Proximal SVRG++ Progress')
plt.grid(True)
plt.show()

#Running time for Proximal SVRG++: 53.30 seconds
