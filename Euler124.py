from math import sqrt
from functools import reduce
from utils import is_prime

def rad(n):
	if n == 1: return 1
	prime_factors = set()
	if n % 2 == 0: prime_factors.add(2)
	elif is_prime(n):prime_factors.add(n)

	for m in range(2, round(sqrt(n)) + 1):
		if n % m == 0:
			if is_prime(m): prime_factors.add(m)
			if is_prime(n/m): prime_factors.add(n/m)
		
	return reduce(lambda x,y : x*y, prime_factors, 1)

collection = []
for n in range(1, 100001):
	collection.append((n, rad(n)))

srtd = sorted(collection, key=lambda tup : tup[1])
print(srtd[9999][0])
