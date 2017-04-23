from math import sqrt

# returns sum of the proper divisors of n
def pdivisor_sum(n):
	s = 1
	for i in range(2, int(sqrt(n)) + 1):
		if sqrt(n) == i:
			s += i
		elif n % i == 0:
			s = s + i + n/i

	return s
	
# 12 is the smallest abundant number
abundants = [12]
#all ints > 28123 can be expressed the sum of 2 abundants
lim = 28123 + 1
for i in range(14, lim):
	
	if pdivisor_sum(i) > i:
		abundants.append(i)


abundant_sums = set()
for i in range(len(abundants)):
	for j in range(len(abundants)):
		abundant_sums.add(abundants[i] + abundants[j])

non_abundant_sums = set(range(1, lim)) - abundant_sums

print(sum(non_abundant_sums))