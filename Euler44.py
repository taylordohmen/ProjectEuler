from math import inf

pent = {n * (3 * n - 1) // 2 for n in range(1, 10000)}
d = inf
for p in pent:
	for q in pent:
		if p - q in pent and p + q in pent and abs(p-q) < d:
			d = abs(p-q)

print(d)
