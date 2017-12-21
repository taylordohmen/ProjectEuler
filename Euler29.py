def distinctPowers(n):
	terms = []
	for i in range(2,n+1):
		for j in range(2,n+1):
			terms.append(i**j)
	return len(set(terms))

print(distinctPowers(100))
