import math

def factorialDigitsum(n):
	summation = 0
	x = math.factorial(n)
	for i in str(x):
		summation += int(i)
	return summation

print(factorialDigitsum(100))
