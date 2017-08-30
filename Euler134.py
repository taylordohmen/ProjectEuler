from math import sqrt

def primes(n):
	N = {i: True for i in range(3, n+1, 2)}
	s = sqrt(n)
	for i in range(3, int(s) + 1, 2):
		if N[i]:
			for j in range(i**2, n + 1, 2*i):
				N[j] = False
	p = [n for n in N if N[n]]
	p.insert(0, 2)
	return sorted(p)

def match(n, m):
	matches = 0
	while m > 0:
		a = n % 10
		b = m % 10
		if a != b:
			return False, matches
		matches += 1
		n //= 10
		m //= 10
	return True, -1

lim = 1000009	
sigma = 0
p = primes(lim)[2:]
for i in range(len(p) - 1):
	p1, p2 = p[i], p[i+1]
	j = 3
	n = p2 * j
	while n % 10 != p1 % 10:
		j += 1
		n = p2 * j
	f = 10
	m = 0
	test, matches = match(n, p1)
	hold = matches
	while not test:
		if matches > hold:
			f *= (10**(matches-hold))
			hold = matches
		j += f
		n = p2 * j
		test, matches = match(n, p1)
	sigma += n

print(sigma)
