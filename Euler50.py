from math import sqrt

def prime(n):
	if n == 2: return True
	if n % 2 == 0: return False
	for i in range(3, int(sqrt(n) + 1), 2):
		if n % i == 0: return False
	return True

p_lst = [n for n in range(2, 10000) if prime(n)]

def longest_prime_prime_sum(n):
	if n == 0: return
	global p_lst
	l = len(p_lst)
	j = l - n
	i = 0
	while j < l:
		j += 1
		i += 1
		sigma = sum(p_lst[i:j])
		if sigma > 1000000: break
		if prime(sigma): return sigma
	return longest_prime_prime_sum(n+1)

print(longest_prime_prime_sum(1))
