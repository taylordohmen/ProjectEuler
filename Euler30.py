def digitFifthPowers(n):
	nums = []
	for i in range(1000,10 ** (n+1)):
		hold = []
		x = str(i)
		for j in x:
			hold.append(int(j)**n)
		if sum(hold) == i:
			nums.append(i)
	return sum(nums)

print(digitFifthPowers(5))
