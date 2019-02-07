import numpy as np
from numpy.linalg import inv

def expBySquaring(x, n):
	if n < 0:
		return expBySquaring(inv(x), - n)
	elif n == 0:
		return 1
	elif n == 1: 
		return x
	elif n % 2 == 0: # Pair case
		return expBySquaring(x.dot(x),  n / 2)
	elif n % 2 == 1: # Odd case
		return x.dot(expBySquaring(x.dot(x), (n - 1) / 2))

n = input('n = ')
m = np.array([[1, 1], [1, 0]], dtype = np.object)
fib_m = expBySquaring(m, int(n) - 1)

print(f'fibonacci({n}) = {fib_m[0, 0]}')