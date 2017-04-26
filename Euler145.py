import re
even_form = re.compile('[13579]*')
def count_range(x, y):
	count = 0
	for n in range(x, y, 2):
		if n % 10 == 0: continue
		some = str(n + int(str(n)[::-1]))
		if even_form.fullmatch(some): count += 2
	return count

# just ran this for each valid |n| -> 2,3,4,6,7,8
# and summed results manually