mx = 0
n = 2
while True:
	i = 2
	s = str(n) + str(n*i)
	if len(s) > 9: break
	while len(s) < 9:
		i += 1
		s = s + str(n*i)
	if sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		mx = int(s)
	n += 1
print(mx)