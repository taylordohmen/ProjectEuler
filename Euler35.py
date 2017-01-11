#Super shitty solution takes almost 30 seconds
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
def testCircPrime(n):
	circPrime = True
	if len(str(n)) < 2:
		circPrime = True
	else:
		x = str(n)
		for k in range(len(x)):
			if testPrime(float(x)) == True:
				y = x[0]
				x = x[1:] + y
			else:
				circPrime = False
	return circPrime
def circularPrimes(n):
	primes = [2]
	numCircPrimes = 0
	for i in xrange(3,n,2):
		if testPrime(i) == True:
			primes.append(i)
	for j in primes:
		if testCircPrime(j) == True:
			numCircPrimes += 1
	return numCircPrimes
print circularPrimes(1000000)