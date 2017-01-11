# finds the sum of all 1-9 pandigital products

singles = [1,2,3,4,5,6,7,8,9]

doubles = []

tripples = []

quads = []

# returns the product if the expression producing it is 1-9 pandigital
# else returns 0
def pandigital(x, y):

	product = x * y
	expression = str(x) + str(y) + str(product)
	
	if len(expression) != 9:
		return 0
	if len(set(expression)) != 9:
		return 0
	if '0' in expression:
		return 0
	return product

# generates all distinct 2, 3, and four digit numbers with no repeating digits and places them in the appropriate lists
for i in singles:
	for j in singles:
		if i != j:
			temp = str(i) + str(j)
			doubles.append(int(temp))
			for k in singles:
				if k != j and k != i:
					othertemp = str(i) + str(j) + str(k)
					tripples.append(int(othertemp))
					for x in singles:
						if x != k and x != j and x != i:
							temp2 = str(i) + str(j) + str(k) + str(x)
							quads.append(int(temp2))

prods = set()

for i in singles:
	for j in quads:
		prods.add(pandigital(i, j))

for i in doubles:
	for j in tripples:
		prods.add(pandigital(i, j))

print(sum(prods))