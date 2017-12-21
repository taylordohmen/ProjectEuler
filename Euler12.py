#Takes about 7 seconds to get the solution....not terrible...
import math

def factorCount(n): #returns the numbers of factors of n
	factors = []
	for i in range(1,int(math.sqrt(n)+1)):
		if n % i == 0:
			factors.append(i)
	return len(factors) * 2
x = [i for i in range(15000)]

def hdtn(x):
	for i in x:
		numFactors = factorCount(sum(x[:i]))
		if numFactors > 500:
			break
	return sum(x[:i])

print(hdtn(x))
