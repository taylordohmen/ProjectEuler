#Runs slightly faster than iterative solution
import math
def testPrime(n):
	prime = True
	if n == 1 or n == 0:
		prime = False
	for i in range(2,int(math.sqrt(n))+1):
		if n % i == 0:
			prime = False
			break
	return prime
def truncateLeft(n):
	x = str(n)
	if len(x) == 1:
		if testPrime(int(x)) == True:
			return True
		else:
			return False
	else:
		if testPrime(int(x)) == True:
			x = x[1:]
			return truncateLeft(x)
		else:
			return False
def truncateRight(n):
	x = str(n)
	if len(x) == 1:
		if testPrime(int(x)) == True:
			return True
		else:
			return False
	else:
		if testPrime(int(x)) == True:
			x = x[:len(x)-1]
			return truncateRight(x)
		else:
			return False
def allTruncatablePrimes():
	primes = []
	for i in range(11,1000000,2):
		if truncateRight(i) == True and truncateLeft(i) == True:
			primes.append(i)
		if len(primes) == 11:
			break
	return sum(primes)
print allTruncatablePrimes()