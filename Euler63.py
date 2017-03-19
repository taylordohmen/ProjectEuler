#counts the number of n-digit integers that can also be represented as an integer to the power of n
count = 0
base = 1
exponent = 1
l = len(str(base ** exponent))
while l <= exponent:
	while l == exponent:
		count += 1
		exponent += 1
		l = len(str(base ** exponent))
	exponent = 1
	base += 1
	l = len(str(base ** exponent))

print(count)