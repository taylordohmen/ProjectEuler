from math import log

def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

# starts at n = 7 and then computes n**m, 1 < m < 10
# if the result, a, is a power of n, then a is added to A
# sorts then finds the 30th element
# limited a to 100 because it was the first lim i picked where
# the resulting set had a cardinatlity > 30

n = 7
A = []
while n < 100:
	m = 2
	a = n ** m
	b = sum_digits(a)
	while m < 10:
		a = n ** m
		b = sum_digits(a)
		if b > 1 and float(round(log(n, b), 10)).is_integer():
			A.append(a)
		m += 1
	n += 1

print(sorted(A)[30])