from fractions import Fraction

e = [1 for i in range(99)]
f = lambda n : 3*n - 1
n = 1
while f(n) - 1 < 99:
	e[f(n) - 1] = 2*n
	n += 1

def real_approx(e):
	if len(e) <= 1: return Fraction(1, e[0])
	return Fraction(1, (e[0] + real_approx(e[1:])))

convergent = Fraction(2, 1) + real_approx(e)
numerator = [int(c) for c in str(convergent.numerator)]
print(sum(numerator))
