from itertools import combinations

def subset_sums(st):
	for i in range(1, len(st) + 1):
		for c in combinations(st, i):
			yield(sum(c), len(c))


def special(st):

	results = set()
	for s, l in subset_sums(st):

		if (s, l) in results:
			return False

		for a, b in results:
			if l > b and s <= a:
				return False

		results |= { (s, l) }

	return True

with open('sets.txt') as file:
	sets = [set(map(int, line.split(','))) for line in file.readlines()]


sigma = 0
for s in sets:
	if special(s):
		sigma += sum(s)

print(sigma)
