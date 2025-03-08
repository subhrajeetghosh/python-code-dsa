import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
d = 1                
n = 100              

xbar = np.random.rand(d)  
s = np.random.rand(n) * 10 - 5  
t = s * xbar + np.random.randn(n)  
S = np.column_stack((s, np.ones(n)))  
x = np.zeros(d + 1)  

L = np.linalg.norm(S.T @ S, 2)  
epsilon = 1 / L                 
omega = 1e-4                    

def gradient(x):
    """Compute the gradient of the objective function."""
    return S.T @ (S @ x - t)

iteration = 0
max_iterations = 10000
while True:
    grad = gradient(x)
    if np.linalg.norm(grad) <= omega or iteration >= max_iterations:
        break
    x = x - epsilon * grad
    iteration += 1

print(f"Converged in {iteration} iterations.")
print(f"Optimal parameters (slope, intercept): {x}")
print(f"Final objective value: {0.5 * np.linalg.norm(S @ x - t)**2}")


plt.plot(s, t, '*', label="Data points")

vec = np.linspace(min(s), max(s), 100)
plt.plot(vec, vec * x[0] + x[1], label=f"Fitted line: y = {x[0]:.2f}x + {x[1]:.2f}")

plt.xlabel("s")
plt.ylabel("t")
plt.legend()
plt.title("Data Fitting using Gradient Descent")
plt.show()