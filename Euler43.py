#runs between 16 and 18 seconds. Pretty slow...
import itertools
def substringDiv():
	num = "1234567890"
	x = list(itertools.permutations(num, len(num)))
	summation = 0
	for i in range(len(x)):
		y = str(x[i])[2::5]
		if int(y[1:4]) % 2 == 0:
			if int(y[2:5]) % 3 == 0:
				if int(y[3:6]) % 5 == 0:
					if int(y[4:7]) % 7 == 0:
						if int(y[5:8]) % 11 == 0:
							if int(y[6:9]) % 13 == 0:
								if int(y[7:10]) % 17 == 0:
									summation += int(y)
	return summation
print substringDiv()