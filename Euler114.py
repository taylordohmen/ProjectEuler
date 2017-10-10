c = {}

def count(n,m):
	global c
	if (n,m) in c:
		return c[(n,m)]
	if m < 3:
		return 0
	if n - m < 4:
		r = n - m + 1 + count(n, m - 1)
		c[(n,m)] = r
		return r
	r = n - m + 1 + sum([count(x, x) for x in range(3, n - m)]) + count (n, m - 1)
	c[(n, m)] = r
	return r

print(count(50,50) + 1)
