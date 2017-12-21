import math

def pythagTrip(m,n):
	finish=0
	a = n**2 - m**2
	b = 2 * n * m
	c = math.hypot(a,b)
	while b < 1000 - 2*n**2:		
		n += 1
		if n % 5 == 0:
			m += 1
		a = n**2 - m**2
		b = 2 * n * m
		c = math.hypot(a,b)
	return a*b*c

print(pythagTrip(1,2))
