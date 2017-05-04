n = 10 ** 8

squares = [1]
i = 2
s = i**2
while s + squares[-1] < n:
	squares.append(s)
	i += 1
	s = i**2

p_sum = set()
for k in range(2, len(squares)):
	i = 0
	j = k
	while j < len(squares):
		x = sum(squares[i:j])
		if x >= n: break
		if str(x) == str(x)[::-1]:
			p_sum.add(x)
		i += 1
		j += 1

print(sum(p_sum))