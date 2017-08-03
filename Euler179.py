from math import sqrt

def primes(n):
	N = {n: True for n in range(3, n+1, 2)}
	s = sqrt(n)
	for i in range(3, int(s) + 1, 2):
		if N[i]:
			for j in range(i**2, n, 2*i):
				N[j] = False
	p = [n for n in N if N[n]]
	p.insert(0,2)
	return p, set(p)

lim = 10**7
p, pset = primes(lim)
facts = {}

def factors(n):
  global p, pset, facts
  f = {}
  i = 0
  m = 2
  while n > 1:
    while n % m == 0:
      f[m] = f[m] + 1 if m in f else 1
      n //= m
    if n in facts:
      f.update(facts[n])
      return f
    if n in pset:
      f[n] = 1
      break
    i += 1
    m = p[i]
  return f

def divisors(f):
  d = 1
  for p in f:
    d *= (f[p] + 1)
  return d

count = 0
for n in range(2, lim):
  f = factors(n)
  f1 = factors(n + 1)
  d = divisors(f)
  d1 = divisors(f1)
  facts[n] = f
  facts[n+1] = f1
  if d == d1:
    # print(n, n+1)
    # print(f, f1)
    count += 1

print(count)
