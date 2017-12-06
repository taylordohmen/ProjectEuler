from math import sqrt
from utils import is_prime

n = 7
primes = 8
while primes/((2*n)-1) >= .10:
	n += 2
	a = n**2 - n + 1
	b = a - n + 1
	c = b - n + 1
	corners = [a,b,c]
	for i in corners:
		if is_prime(i):
			primes += 1

print(n)
