from utils import primes_up_to

lim = 1000001

P, pset = primes_up_to(lim)

def prime_factors(n):
	global P, pset
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
