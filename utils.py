from math import sqrt

# RETURNS <boolean> n's primality
def is_prime(n):
  if n < 2: return False
  if n == 2: return True
  if n % 2 == 0: return False
  for m in range(3, int(sqrt(n)) + 1, 2):
    if n % m == 0: return False
  return True

# RETURN <list>, <set> of prime numbers <= n
def primes_up_to(n):
	N = {n: True for n in range(3, n+1, 2)}
	s = sqrt(n)
	for i in range(3, int(s) + 1, 2):
		if N[i]:
			for j in range(i**2, n + 1, 2*i):
				N[j] = False
	p = [n for n in N if N[n]]
	p.insert(0,2)
	return p, set(p)

# RETURN <list> of the 1st n primes
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

# RETURN <set> of integer factors of n, 1 < f < n
def factors(n):
	f = set()
	for m in range(2, int(sqrt(n)) + 1):
		if n % m == 0:
			f |= {m, n//m}
	return f
