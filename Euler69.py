from math import sqrt

lim = 1000001

def primes(n):
	P = [2]
	pset = {2}
	p = 3
	while len(P) < n:
		i = 0
		prime = True
		s = sqrt(p)
		while P[i] <= s:
			if p % P[i] == 0:
				prime = False
				break
			i += 1
		if prime:
			P.append(p)
			pset.add(p)
		p += 2
	return P, pset

P, pset = primes(20 * int(sqrt(lim)) + 1)

def prime_factors(n):
	global P
	f = {}
	i = 0
	m = 2
	while n > 1:
		if n % m == 0:
			f[m] = 1
			n //= m
		while n % m == 0:
			f[m] += 1
			n //= m
		if n in pset:
			f[n] = 1
			break
		i += 1
		m = P[i]
	return f

def phi(n):
	coprime = 1
	if n in pset:
		return coprime
	primes = prime_factors(n)
	for p in primes:
		if primes[p] > 1:
			coprime *= p**primes[p]*(p - 1)
		else:
			coprime *= (p-1)
	return coprime

N = 0
Q = 0
for n in range(30, lim, 30):
	p = phi(n)
	q = n / p
	if q > Q:
		Q = q
		N = n

print(N)
