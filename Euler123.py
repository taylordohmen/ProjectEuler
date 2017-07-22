from math import sqrt

def primes(n):
	P = [2]
	p = 3
	while len(P) < n:
		i = 0
		prime = True
		while P[i] <= sqrt(p):
			if p % P[i] == 0:
				prime = False
				break
			i += 1
		if prime:
			P.append(p)
		p += 2
	return P

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
