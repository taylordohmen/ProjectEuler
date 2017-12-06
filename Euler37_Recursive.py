#Runs slightly faster than iterative solution
import math
from utils import is_prime

def truncateLeft(n):
	x = str(n)
	if len(x) == 1:
		if is_prime(int(x)) == True:
			return True
		else:
			return False
	else:
		if is_prime(int(x)) == True:
			x = x[1:]
			return truncateLeft(x)
		else:
			return False

def truncateRight(n):
	x = str(n)
	if len(x) == 1:
		if is_prime(int(x)) == True:
			return True
		else:
			return False
	else:
		if is_prime(int(x)) == True:
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

print(allTruncatablePrimes())
