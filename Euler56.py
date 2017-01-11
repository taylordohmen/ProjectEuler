def powerfulDigitSum():
	sums = []
	nums = []
	for i in xrange(2,101):
		for j in xrange(2,101):
			nums.append((i,j))
			x = str(i ** j)
			y = 0
			for k in x:
				y += int(k)
			sums.append(y)
	print nums[sums.index(max(sums))]
	return max(sums)
print powerfulDigitSum()