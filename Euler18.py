txt = open('Euler18.txt','r')
txt = txt.readlines()
txt.remove(txt[0])
newTxt = []

for i in txt:
	newTxt.append(i[:len(i)-1])

def maxPathSum(pyramid): #pyramid is a list containing strings. each string is a line of the triangle
	sums = []
	if len(pyramid) == 1:
		z = pyramid[-1].split(' ')
		a = []
		for j in z:
			a.append(int(j))
		return max(a) + 75  #75 is just the number at the top of the triangle
	else:
		x = pyramid[-1].split(' ')
		y = pyramid[-2].split(' ')
		for k in range(len(y)):
			sums.append(int(y[k]) + int(x[k]))
			sums.append(int(y[k]) + int(x[k+1]))
		pyramid = pyramid[:-1]
		newSums = []
		for r in range(0,len(sums),2):
			if sums[r] > sums[r+1]:
				newSums.append(sums[r])
			else:
				newSums.append(sums[r+1])
		pyramid[-1] = str(newSums)[1:-1]
		pyramid[-1] = pyramid[-1].replace(',','')
		return maxPathSum(pyramid)

print(maxPathSum(newTxt))
