from utils import is_prime

def testCircPrime(n):
	circPrime = True
	if len(str(n)) < 2:
		circPrime = True
	else:
		x = str(n)
		for k in range(len(x)):
			if is_prime(int(x)) == True:
				y = x[0]
				x = x[1:] + y
			else:
				circPrime = False
	return circPrime

def circularPrimes(n):
	primes = [2]
	numCircPrimes = 0
	for i in range(3,n,2):
		if is_prime(i) == True:
			primes.append(i)
	for j in primes:
		if testCircPrime(j) == True:
			numCircPrimes += 1
	return numCircPrimes

print(circularPrimes(1000000))
