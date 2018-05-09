from math import sqrt

def sqrt_real_part_sum(n, precision):
	root = int(sqrt(n))
	if root == sqrt(n):
		return 0
	
	sigma = root
	place = 1
	while place < precision:
		
		digit = 9
		new_root = root * 10 + digit
		ideal = n * 10**(2*place)

		while new_root**2 > ideal:
			digit -= 1
			new_root = root * 10 + digit
			ideal = n * 10**(2*place)
			
		sigma += digit
		root = new_root
		place += 1

	return sigma

sigma = 0
for n in range(1, 101):
	sigma += sqrt_real_part_sum(n, 100)

print(sigma)
