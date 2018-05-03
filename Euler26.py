def cycle_len(denominator, lim):	

	quotient = str(1 / denominator)
	if len(quotient) < 10:
		return 0

	rep_word = str(10**lim // denominator)
	for i in range(len(rep_word)):

		if rep_word[ -i : ] == rep_word[ -2 * i : -i ]:
			return i

lim = 1000
long, big_d = 1, 0
for d in range(2, lim):

	cl = cycle_len(d, 2 * lim)
	if cl > long:
		long, big_d = cl, d

print(big_d)
