def wayBetterSolution(n,r):
	return sum([int(i) for i in str(n ** r)])

print(wayBetterSolution(2,1000))