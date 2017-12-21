def fibo(n):
	x = 1
	y = 1
	z = x + y
	count = 3
	while len(str(z)) < n:
		if count % 2 == False:
			x = z
		else:
			y = z
		z = y + x
		count += 1
	return count

print(fibo(1000))
