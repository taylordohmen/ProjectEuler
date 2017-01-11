#Runs slightly slower than recursive solution
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
	verdict = True
	for i in range(len(x)):
		if testPrime(int(x[i:])) != True:
			verdict = False
			break
	return verdict
def truncateRight(n):
	x = str(n)
	verdict = True
	for i in range(len(x)):
		if testPrime(int(x[:len(x) - i])) != True:
			verdict = False
			break
	return verdict
def allTruncatablePrimes():
	primes = []
	for i in xrange(11,1000000,2):
		if truncateRight(i) == True and truncateLeft(i) == True:
			primes.append(i)
		if len(primes) == 11:
			break
	return sum(primes)
print allTruncatablePrimes()