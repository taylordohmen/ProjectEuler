def powerdigitSum(n,r):
	product = n ** r
	productStr = str(product)
	hold = []
	for i in productStr:
		x = int(i)
		hold.append(x)
	summation = sum(hold)
	return summation
print powerdigitSum(2,1000)

def wayBetterSolution(n,r):
	return sum([int(i) for i in str(n ** r)])
print wayBetterSolution(2,1000)