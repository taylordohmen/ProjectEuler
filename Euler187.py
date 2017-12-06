from math import sqrt
from utils import primes_up_to

lim = 10**8
p = primes_up_to(lim)[0]
c = 0
i = 0
while p[i] * p[i] < lim:
	j = i
	while p[i] * p[j] < lim:
		c += 1
		j += 1
	i += 1

print(c)
