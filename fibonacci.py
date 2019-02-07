import numpy as np
from numpy.linalg import inv

def expBySquaring(x, n):
	if n == 1:
		return x
	if n % 2 == 0:
		return expBySquaring(x.dot(x), n // 2)
	return x.dot(expBySquaring(x.dot(x), n // 2))

n = int(input('n = '))
m = np.array([[1, 1], [1, 0]], dtype = np.object)

if n > 1:
	fib_m = expBySquaring(m, n - 1)
elif n == 1:
	fib_m = np.array([[1, 0], [0, 0]], dtype = np.object)
elif n == 0:
	fib_m = np.array([[0, 0], [0, 0]], dtype = np.object)

print(f'fibonacci({n}) = {fib_m[0, 0]}')