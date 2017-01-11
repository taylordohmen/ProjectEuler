def smallestPermutedMultiple():
	for j in xrange(1,1000000):
		match = False
		string = str(j)
		for i in xrange(2,7):	
			x = str(int(string) * i)
			if set(string) == set(x):
				match = True
			else:
			    match = False
			    break
		if match == True:
			break
	return string
print smallestPermutedMultiple()