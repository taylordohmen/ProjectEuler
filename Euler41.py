from itertools import permutations
from math import sqrt

def prime(n):
	if n % 2 == 0: return False
	for i in range(3, int(sqrt(n)) + 1, 2):
		if n % i == 0: return False
	return True

p = 0
# there are no prime 8 or 9 digit pandigitals
for s in permutations('7654321'):
	n = int(''.join(s))
	if prime(n):
		p = n
		break
print(p)