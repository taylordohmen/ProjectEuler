from math import sqrt
from utils import is_prime

primes = 0
n = 1
p = 0
num = 2
denom = 1
lim = 1000000
while p < lim:
  m = round(n**3 * num / denom)
  p = round((m**3 - n**9) / n**6)
  if is_prime(p):
    primes += 1
  n, num, denom = n+1, num+1, denom+1

print(primes)
