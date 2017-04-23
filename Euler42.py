def wordScore(word):# finds word score
	alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	score = 0
	for i in word:
		score += (alph.index(i) + 1)
	return score

def reverseTriangle(score): # evaluates wether word score is a triangle number
	t = False
	for n in range(score):
		if 0.5*n*(n+1) == score:
			t = True
	if score == 1:
		t = True
	return t

def ctn(): #reads in words from file and calls previous two functions
	txt = open('words.txt', 'r')# returns the number of triangle words
	words = txt.read().split(',')
	print words
	count = 0
	for i in words:
		if reverseTriangle(wordScore(i)) == True:
			count += 1
	return count
print ctn()