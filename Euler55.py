# counts the number of lychrel numbers < 10000

lychrels = 0

for i in range(1, 10000):
	iters = 0
	n = i
	m = int(str(n)[::-1])

	while iters < 50:
		n = n + m
		m = int(str(n)[::-1])
		iters += 1

		if str(n) == str(m):
			break

	if iters >= 50:
		lychrels += 1

print(lychrels)
