from math import sqrt

def prime(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0: return False
	for m in range(3, round(sqrt(n))+1, 2):
		if n % m == 0: return False
	return True

def squares_lt(n):
	m = 1
	s = m ** 2
	while s < n / 2:
		yield s
		m += 1
		s = m ** 2

n = 35
smallest = -1
while smallest < 0:
	i = 0
	for s in squares_lt(n):
		if prime(n - 2 * s):
			i += 1
	if i == 0 and not prime(n):
		smallest = n
	n += 2

print(smallest)
