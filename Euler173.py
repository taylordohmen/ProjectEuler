lim = 1000000
count = 0
S = 3
while True:
	hold = count
	s = S
	p = 4*(S-1)
	while p <= lim and s >= 3:
		count += 1
		s -= 2
		p += 4*(s-1)
	if count == hold:
		break
	S += 1

print(count)
