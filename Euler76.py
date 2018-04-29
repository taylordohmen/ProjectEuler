def paritions(n, m, cache):
	if m == 0:
		return 0
	if n == 0:
		return 1
	if n < 0:
		return 0

	if (n, m) in cache:
		return cache[(n, m)]

	cache[(n, m)] = paritions(n, m - 1, cache) + paritions(n - m, m, cache)
	return cache[(n, m)]

print(paritions(100, 99, {}))
