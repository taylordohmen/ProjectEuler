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
def testPerm(x,y):
	z = str(x)
	yesno = True
	for i in z:
		if i in str(y):
			continue
		else:
			yesno = False
	return yesno
def primePermutations():
	primes = []
	x = 0
	for i in xrange(1000,9999):
		if testPrime(i) == True:
			primes.append(i)
	for j in primes:
		if j+3330 in primes and j+6660 in primes and testPerm(j,j+3330) == True\
		 and testPerm(j,j+6660) == True and j != 1487:
			x = j
			break
	return str(j) + str(j+3330) + str(j+6660)
print primePermutations()