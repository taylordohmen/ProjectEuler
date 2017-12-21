from functools import reduce
from math import sqrt
from utils import primes_up_to

lim = 51
rows = [[1]]

for i in range(lim - 1):
	prev = rows[i]
	subseq = []
	for j in range(len(prev) + 1):
		if j in (0, len(prev)):
			subseq.append(1)
		else:
			subseq.append(prev[j-1] + prev[j])
	rows.append(subseq)

nums = reduce(lambda x,y: x.union(y), rows, set())
primes, pset = primes_up_to(int(sqrt(max(nums))) + 1)
sqrs = [p**2 for p in primes]

sqrfreesum = 0

for n in nums:
	sqr = False
	for s in sqrs:
		if n % s == 0:
			sqr = True
			break
	if not sqr:
		sqrfreesum += n

print(sqrfreesum)
