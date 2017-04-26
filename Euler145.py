import re
odd_form = re.compile('[13579]*')
def count_range(x, y):
	count = 0
	for n in (i for i in range(x, y, 2) if i % 10 != 0):
		some = str(n + int(str(n)[::-1]))
		if odd_form.fullmatch(some): count += 2
	return count

print(count_range(1, 1000))

# just ran this func once per valid |n| so 3,4,6,7,8 and added them up
# not an awesome solution but a solution none the less