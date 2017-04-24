from math import sqrt

def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

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
print(primes/((2*n)-1))