from math import sqrt

def prime(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0: return False
	for m in range(3, round(sqrt(n)) + 1, 2):
		if n % m == 0: return False
	return True

def distinct_prime_factors(n):
	dpf = 0
	for m in range(2, round(sqrt(n)) + 1):
		if n % m == 0:
			if prime(m):
				dpf += 1
			if prime(n/m):
				dpf += 1
	return dpf

n = 1000
while True:
	i = [x for x in range(n, n+4) if distinct_prime_factors(x) == 4]
	if len(i) == 4: break
	n += 1
print(n)
