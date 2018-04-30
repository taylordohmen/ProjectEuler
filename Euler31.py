def paritions(n, m, cache):
	if m == 0:
		return 0
	if n == 0:
		return 1
	if n < 0:
		return 0

	vals = [ 0, 1, 2, 5, 10, 20, 50, 100, 200 ]

	if (n, m) in cache:
		return cache[(n, m)]

	cache[(n, m)] = paritions(n, vals[vals.index(m) - 1], cache) + paritions(n - m, m, cache)
	return cache[(n, m)]

print(paritions(200, 100, {}))
