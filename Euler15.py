import math
def latticePaths(n):
	return math.factorial(2*n) / (math.factorial(n)) ** 2
print latticePaths(20)