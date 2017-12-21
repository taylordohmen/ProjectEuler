def nsd(n):# n has got to be an odd number
	summation = 0
	x = 1
	inc = 2
	while x < n**2:
		for i in range(4):
			summation += x
			x += inc
		inc += 2
	return summation + n**2

print(nsd(1001))
