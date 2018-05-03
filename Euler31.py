def partitions(n, m, cache):
	if m == 0:
		return 0
	if n == 0:
		return 1
	if n < 0:
		return 0

	vals = [ 0, 1, 2, 5, 10, 20, 50, 100, 200 ]

	if (n, m) in cache:
		return cache[(n, m)]

	cache[(n, m)] = partitions(n, vals[vals.index(m) - 1], cache) + partitions(n - m, m, cache)
	return cache[(n, m)]

print(partitions(200, 100, {}))
