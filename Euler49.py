import math
from utils import is_prime

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
	for i in range(1000,9999):
		if is_prime(i) == True:
			primes.append(i)
	for j in primes:
		if j+3330 in primes and j+6660 in primes and testPerm(j,j+3330) == True\
		 and testPerm(j,j+6660) == True and j != 1487:
			x = j
			break
	return str(j) + str(j+3330) + str(j+6660)

print(primePermutations())
