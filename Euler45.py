import math
def triangle(t):
	return (t*(t+1))/2
def pentagonal(p):
	return (p*(3*p - 1))/2
def hexagonal(h):
	return h*(2*h - 1)
def tph(t,p,h):
	while triangle(t) != pentagonal(p) or triangle(t) != hexagonal(h):
		t += 1
		while pentagonal(p) < triangle(t):
			p += 1
		while hexagonal(h) < triangle(t):
			h += 1
	return triangle(t)
print tph(286,166,143)			