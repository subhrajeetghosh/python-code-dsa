import numpy as np
import scipy.io
import time
import matplotlib.pyplot as plt

np.random.seed(123)
data = scipy.io.loadmat('mushrooms.mat')
A = data['A']
b = data['b'].ravel()
n, m = A.shape

omega = 1e-5
K = 10 * n

x = np.zeros(m)
x_prev_epoch = x.copy()
ratios = []

start = time.time()
for k in range(1, K+1):
    i = np.random.randint(n)
    ai = A[i, :]
    bi = b[i]

    z  = bi * ai.dot(x)
    gi = -bi * ai / (1 + np.exp(z))

    eps = 0.1 / np.sqrt(k)

    gi_dense = gi.toarray()

    gi_dense = gi_dense.reshape(x.shape)

    y = x - eps * gi_dense
    x = np.sign(y) * np.maximum(np.abs(y) - omega * eps, 0)

    if k % n == 0:
        ratio = np.linalg.norm(x - x_prev_epoch, 1) / eps
        ratios.append(ratio)
        x_prev_epoch = x.copy()

end = time.time()
print(f"Prox-SGD main loop time: {end - start:.2f} s")

plt.figure(figsize=(6,4))
plt.plot(range(1, 11), ratios, marker='o')
plt.xlabel('Epoch')
plt.ylabel(r'$\|x^{(k)} - x^{(k-1)}\|_1 / \varepsilon_k$')
plt.title('Prox-SGD convergence per epoch')
plt.grid(True)
plt.show()

#Prox-SGD main loop time: 50.36 s
