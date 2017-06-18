def cubic_perms(n):
	C = n**3
	c = sorted(str(C))
	L = len(str(C))
	l = L
	p = 1
	while l == L:
		n += 1
		cube = n**3
		l = len(str(cube))
		if sorted(str(cube)) == c:
			p += 1

	return p

n = 345
p = cubic_perms(n)
while p < 5:
	n += 1
	p = cubic_perms(n)
print(n**3)
