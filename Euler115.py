c = {}

def count(n, m, lim):
	global c
	if (n,m) in c:
		return c[(n,m)]
	if m < lim:
		return 0
	if n - m < 4:
		r = n - m + 1 + count(n, m - 1, lim)
		c[(n,m)] = r
		return r
	r = n - m + 1 + sum([count(x, x, lim) for x in range(3, n - m)]) + count (n, m - 1, lim)
	c[(n, m)] = r
	return r

lim = 50
n = lim * 2
fill_count = count(n, n, lim)
while fill_count < 10**6:
	n += 1
	fill_count = count(n, n, lim)
print(n)
