from math import factorial as fact

def digit_fact_sum(n):
	s = 0
	while n:
		s += fact(n % 10)
		n //= 10
	return s

chains = {}
sixties = 0
for n in range(1, 1000000):
	chain = {n}
	m = digit_fact_sum(n)
	while m not in chain:
		if m in chains:
			chain |= chains[m]
			break
		chain.add(m)
		m = digit_fact_sum(m)
	chains[n] = chain
	if len(chain) == 60:
		sixties += 1

print(sixties)
