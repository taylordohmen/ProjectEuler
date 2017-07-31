from math import sqrt

def factors(n):
  yield 1, n
  for m in range(2, int(sqrt(n) + 1)):
    if n % m == 0:
      yield m, n//m

def triples(r):
  for s, t in factors(r**2//2):
    x = r + s
    y = r + t
    z = r + s + t
    yield x + y + z

perimeters = {}
r = 2
P = 0
while P <= 1000:
  for p in triples(r):
    if p in perimeters:
      perimeters[p] += 1
    else:
      perimeters[p] = 1
    P = p
  r += 2

print(max(perimeters.items(), key=lambda x: x[1])[0])
