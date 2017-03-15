from math import sqrt

# returns sum of the proper divisors of n
def pdivisor_sum(n):
	s = 0
	for i in range(2, int(sqrt(n))):
		if n % i == 0:
			s = s + i + int(n/i)
		if (int(sqrt(n))**2 == n):
			s += 1
	return s + 1

amicables = set()

for i in range(2, 10000):
	x = pdivisor_sum(i)
	y = pdivisor_sum(x)
	if i == y and i != x:
		amicables.add(i)
		amicables.add(y)

print(sum(amicables))