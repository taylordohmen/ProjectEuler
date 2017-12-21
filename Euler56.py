def powerfulDigitSum():
	sums = []
	nums = []
	for i in range(2,101):
		for j in range(2,101):
			nums.append((i,j))
			x = str(i ** j)
			y = 0
			for k in x:
				y += int(k)
			sums.append(y)
	return max(sums)

print(powerfulDigitSum())
