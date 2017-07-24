from math import sqrt

def prime(n):
  if int(n) != n: return False
  if n < 2: return False
  if n == 2: return True
  if n % 2 == 0: return False
  for m in range(3, int(sqrt(n)) + 1, 2):
    if n % m == 0: return False
  return True

primes = 0
n = 1
p = 0
num = 2
denom = 1
lim = 1000000
while p < lim:
  m = round(n**3 * num / denom)
  p = round((m**3 - n**9) / n**6)
  if prime(p):
    primes += 1
  n, num, denom = n+1, num+1, denom+1

print(primes)
