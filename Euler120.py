def r_max(a):
	R = 0
	n = 1
	i = ((a-1)**n + (a+1)**n) % a**2
	n += 1
	r = ((a-1)**n + (a+1)**n) % a**2
	while i != r:
		n += 1
		r = ((a-1)**n + (a+1)**n) % a**2
		if r > R: R = r
	return R

S = 0
for a in range(3, 1001):
	S += r_max(a)
print(S)
