def isPalindrome(x):
	number = str(x)
	if (len(number) == 1 or len(number) == 0):
		return True
	elif (number[0] != number[len(number) - 1]):
		return False
	elif (number[0] == number[len(number) - 1]):
		newNumber = number[1:len(number) - 1]
		return isPalindrome(newNumber)
def doubleBasePalins(n):
	palins = []
	for i in range(1,n,2):
		if isPalindrome(i) == True and isPalindrome(bin(i)[2:]) == True:
			palins.append(i)
	return sum(palins)
print doubleBasePalins(1000000)