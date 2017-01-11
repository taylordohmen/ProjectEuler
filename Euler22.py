def wordScore(word):# finds word score
	alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	score = 0
	for i in word:
		score += (alph.index(i) + 1)
	return score
def nameScores(): #alphabetizes and sums all scores
	txt = open('Euler22_names.txt', 'r')
	txt = txt.read().split(',')
	txt = sorted(txt, key = str)
	score = 0
	totalScore = 0
	for i in txt:
		score = wordScore(i) * (txt.index(i) + 1)
		totalScore += score
	return totalScore
print nameScores()