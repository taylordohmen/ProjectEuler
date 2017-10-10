c = {}
def count(n,m):
	if (n,m) in c:
		return c[(n,m)]
	if n - m < m:
		r = n - m + 1
		c[(n,m)] = r
		return r
	r = n - m + 1 + sum([count(x, m) for x in range(m, n - m + 1)])
	c[(n, m)] = r
	return r

print(count(50, 2) + count(50, 3) + count(50, 4))
