from operator import add, sub, mul, truediv
from itertools import permutations, combinations, product

def longest_sequence(st):
	possible = { n for n in range(1, max(st) + 1) }
	return min(possible - st)

def evaluate(digits, ops):
	a, b, c, d = digits
	x, y, z = ops
	yield x(y(z(a, b),c),d)
	yield x(y(a, b),z(c, d))
	yield x(y(a,z(b, c)),d)

def evaluations(digits):
	operations = [ add, sub, mul, truediv ]
	evals = set()

	for ordered_digits in permutations(digits, 4):
		for ordered_ops in product(operations, repeat=3):

			for val in evaluate(ordered_digits, ordered_ops):
				if val > 0 and int(val) == val:
					evals |= { val }

	return evals

digits = [ n for n in range(1, 10) ]
long_seq_digits = None
longest = 0

for c in combinations(digits, 4):
	evals = evaluations(c)
	seq_len = longest_sequence(evals)

	if seq_len > longest:
		longest = seq_len
		long_seq_digits = c

print(long_seq_digits)
