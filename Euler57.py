from fractions import Fraction

def real_approx(n):
	d = Fraction(1, 2)
	for i in range(n-1):
		d = Fraction(1, 2 + d)
	return d

count = 0
for n in range(1, 1001):
	approx = Fraction(1,1) + real_approx(n)
	if len(str(approx.numerator)) > len(str(approx.denominator)):
		count += 1
print(count)
