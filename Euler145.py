import re
even_form = re.compile('[13579]*')
def count_range(x, y):
	count = 0
	for n in range(x, y):
		if n % 10 == 0: continue
		some = str(n + int(str(n)[::-1]))
		if even_form.fullmatch(some): count += 1
	return count

# just ran this func once per valid |n| so 3,4,6,7,8 and added them up
# not an awesome solution but a solution none the less