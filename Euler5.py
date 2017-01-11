#Incredibly inefficient solution
def checkDivisibility(x):
	for i in range(11,20):
		if(x % i != 0):
			return False
	return True
def numSearch(lbound, ubound):
	for i in range(lbound,ubound,20):
		if(checkDivisibility(i) == True):
			return i
print(numSearch(1000000,465585120))
