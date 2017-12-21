txt = open('Euler79.txt', 'r')
txt = txt.read().split()
holdlist = []
for i in txt:
	for j in i:
		holdlist.append(j)
holdlist = list(set(holdlist))
print(holdlist)

#73162890 Solved this one using my brain, didn't solve with the code

