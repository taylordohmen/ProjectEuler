from math import sqrt

def primes(n):
	N = {n: True for n in range(3, n+1, 2)}
	s = sqrt(n)
	for i in range(3, int(s) + 1, 2):
		if N[i]:
			for j in range(i**2, n, 2*i):
				N[j] = False
	p = [n for n in N if N[n]]
	p.insert(0,2)
	return p

lim = 10**8
p = primes(lim)
c = 0
i = 0
while p[i] * p[i] < lim:
	j = i
	while p[i] * p[j] < lim:
		c += 1
		j += 1
	i += 1

print(c)
