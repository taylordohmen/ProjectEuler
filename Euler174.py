lim = 1000000
N = {}
S = 3
while True:
	hold = False
	s = S
	p = 4*(S-1)
	while p <= lim and s >= 3:
		hold = True
		N[p] = N[p] + 1 if p in N else 1
		s -= 2
		p += 4*(s-1)
	if not hold:
		break
	S += 1

print(len([i for i in N if N[i] <= 10 and N[i] >= 1]))
