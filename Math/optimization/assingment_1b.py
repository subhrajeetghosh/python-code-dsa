import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import time
import scipy.sparse as sp

np.random.seed(123)
data = scipy.io.loadmat('mushrooms.mat')
A = data['A']            # (n, m) sparse matrix
b = data['b'].reshape(-1) # (n,) vector
n, m = A.shape
lam = 1e-5

L = 0
for i in range(n):
    ai = A[i, :].toarray().flatten()
    L = np.maximum(L, np.linalg.norm(ai))
L = (L ** 2) / 4

epsilon = 1 / (3 * L)

x = np.zeros(m)
grad_table = np.zeros((n, m))
full_grad = np.zeros(m)

for i in range(n):
    ai = A[i, :].toarray().flatten()
    bi = b[i]
    s = bi * ai.dot(x)
    grad_i = -bi * ai / (1 + np.exp(s))
    grad_table[i, :] = grad_i
full_grad = np.mean(grad_table, axis=0)

def prox_l1(v, lam):
    return np.sign(v) * np.maximum(np.abs(v) - lam, 0.0)

norm_diffs = []
iters_per_epoch = n
epochs = 10
total_iters = iters_per_epoch * epochs

start_time = time.time()

for k in range(total_iters):
    x_old = x.copy()

    i = np.random.randint(0, n)
    ai = A[i, :].toarray().flatten()
    bi = b[i]

    s = bi * ai.dot(x)
    grad_i_new = -bi * ai / (1 + np.exp(s))

    grad = grad_i_new - grad_table[i, :] + full_grad

    x = x - epsilon * grad

    x = prox_l1(x, epsilon * lam)

    full_grad += (grad_i_new - grad_table[i, :]) / n
    grad_table[i, :] = grad_i_new

    if (k + 1) % iters_per_epoch == 0:
        diff_norm = np.linalg.norm(x - x_old) / epsilon
        norm_diffs.append(diff_norm)

running_time = time.time() - start_time
print(f"Running time for Proximal SAGA: {running_time:.2f} seconds")

plt.figure(figsize=(8,6))
plt.plot(range(1, epochs+1), norm_diffs, marker='o')
plt.xlabel('Epoch')
plt.ylabel(r'$\|x_k - x_{k-1}\| / \epsilon$')
plt.title('Proximal SAGA Progress')
plt.grid(True)
plt.show()

#Running time for Proximal SAGA: 22.72 seconds