def champernowne():
	hold = ""
	index = (1,10,100,1000,10000,100000,1000000)
	product = 1
	for i in range(1000001):
		hold += str(i)
	for j in index:
		product *= int(hold[j])
	return product
print champernowne()