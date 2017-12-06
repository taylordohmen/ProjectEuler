from math import sqrt
from utils import primes_up_to

lim = 10**7
p, pset = primes_up_to(lim)
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
    count += 1

print(count)
