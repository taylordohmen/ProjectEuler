import math
def digitFactorials():
	nums = []
	for i in range(5,1000000,5):
		hold = []
		for j in str(i):
			hold.append(math.factorial(int(j)))
		if sum(hold) == i:
			nums.append(i)
	return sum(nums)
print digitFactorials()