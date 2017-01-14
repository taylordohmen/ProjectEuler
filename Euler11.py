import functools

with open('Euler11_grid.txt', 'r') as f:
	grid = f.readlines()
side_len = len(grid)

grid = [row.strip('\n').split(' ') for row in grid]
for i in range(side_len):
	for j in range(side_len):
		grid[i][j] = int(grid[i][j])

greatest_prod = 0
mult = lambda a,b: a*b

for i in range(side_len):
	for j in range(side_len):
		
		prods = []
		
		if j < side_len - 4:
			# HORIZONTAL
			prods.append(functools.reduce(mult, grid[i][j:j+4]))
		
		if i < side_len - 4:
			# \ DIAGONAL
			prods.append(functools.reduce(mult, [grid[x][j] for x in range(i, i+4)]))

		if i < side_len - 4 and j < side_len - 4:
			# VERTICAL
			prods.append(functools.reduce(mult, [grid[i][j+x] for x in range(4)]))

			if j >= 3:
				# / DIAGONAL
				prods.append(functools.reduce(mult, [grid[i+x][j-x] for x in range(4)]))

		for k in prods:
			if k > greatest_prod: greatest_prod = k
		
print(greatest_prod)