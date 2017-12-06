from math import sqrt
from utils import primes

def R(n, p):
	return ((p[n]-1)**n + (p[n]+1)**n) % p[n]**2

p = primes(50000)
n = len(p) // 2 - 1
N = [0]
h = len(p)
l = 0
r = R(n, p)
lim = 10**10
while n != N[-1]:
	N.append(n)
	if r < lim:
		l = n
	if r > lim:
		h = n
	n = (h + l) // 2
	while n % 2 == 0:
		n += 1

	r = R(n, p)

print(n + 2)
