def selfPowers(n):
	x = []
	for i in range(1,n+1):
		x.append(i**i)
	y = str(sum(x))
	return y[-10:]

print(selfPowers(1000))
