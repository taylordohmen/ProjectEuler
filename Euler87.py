from math import sqrt

def prime(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for m in range(3, round(sqrt(n)) + 1, 2):
		if n % m == 0:
			return False
	return True 

lim = 50000000
a_lim = round(lim**(1/2))
b_lim = round(lim**(1/3))
c_lim = round(lim**(1/4))
a = 2
b = 2
c = 2
count = set()
while c < c_lim:
	s = a**2 + b**3 + c**4
	if s < lim:
		count.add(s)
	while b < b_lim:
		if s < lim:
			count.add(s)
		s = a**2 + b**3 + c**4
		while a < a_lim:
			if s < lim:
				count.add(s)
			s = a**2 + b**3 + c**4
			a = a + 1 if a == 2 else a + 2
			while not prime(a):
				a = a + 1 if a == 2 else a + 2
		a = 2
		b = b + 1 if b == 2 else b + 2
		while not prime(b):
			b = b + 1 if b == 2 else b + 2
	b = 2
	c = c + 1 if c == 2 else c + 2
	while not prime(c):
		c = c + 1 if c == 2 else c + 2

print(len(count))
