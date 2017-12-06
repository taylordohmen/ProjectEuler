#Runs slightly slower than recursive solution
import math
from utils import is_prime

def truncateLeft(n):
	x = str(n)
	verdict = True
	for i in range(len(x)):
		if is_prime(int(x[i:])) != True:
			verdict = False
			break
	return verdict

def truncateRight(n):
	x = str(n)
	verdict = True
	for i in range(len(x)):
		if is_prime(int(x[:len(x) - i])) != True:
			verdict = False
			break
	return verdict

def allTruncatablePrimes():
	primes = []
	for i in range(11,1000000,2):
		if truncateRight(i) == True and truncateLeft(i) == True:
			primes.append(i)
		if len(primes) == 11:
			break
	return sum(primes)

print(allTruncatablePrimes())
