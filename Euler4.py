def isPalindrome(x):
	number = str(x)
	if (len(number) == 1 or len(number) == 0):
		return True
	elif (number[0] != number[len(number) - 1]):
		return False
	elif (number[0] == number[len(number) - 1]):
		newNumber = number[1:len(number) - 1]
		return isPalindrome(newNumber)

def greatestPalindromeProduct(x):
	for i in range(x, x - 100, -1):
		product = x * i
		if(isPalindrome(product) == True):
			return product
	return greatestPalindromeProduct(x - 1)

print(greatestPalindromeProduct(999))
