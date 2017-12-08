from utils import primes_up_to
from math import sqrt

lim = 10**7
P, pset = primes_up_to(lim//2)

N = 0
Q = 10

for i in range(len(P)):
	for j in range(i, len(P)):

		n, m = P[i], P[j]
		x = n * m

		if x >= lim: break

		p = (x - 1) - (n - 1) - (m - 1)

		if p < 1: continue

		q = x / p
		if q < Q and sorted(str(x)) == sorted(str(p)):
			Q = q
			N = x

print(N, Q)
