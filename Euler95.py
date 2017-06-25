from math import sqrt

def divisor_sum(n):
	ds = 1
	for m in range(2, round(sqrt(n))):
		if n % m == 0:
			ds += m + n//m
	return ds

chains = {}
longest = [1]
n = 2
while max(longest) < 100000:
	chain = [n]
	m = divisor_sum(n)
	while m != n  and m not in chain and m > 1 and m < 1000000:
		if m in chains:
			chain += chains[m]
			break
		chain.append(m)
		m = divisor_sum(m)
	chains[n] = chain
	if chain[-1] == chain[0] and len(chain) > len(longest):
		longest = chain
	n += 1

print(min(longest))
