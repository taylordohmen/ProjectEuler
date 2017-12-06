from math import sqrt
from utils import is_prime

def A(n):
  r = 111
  rep_len = 3
  r_mod = r % n
  while r_mod != 0:
    r = r * 10 + 1
    r_mod = ((r_mod * (10%n) % n) + (1 % n)) % n
    rep_len += 1
  return rep_len

N = []
n = 91
while len(N) < 25:
  if not is_prime(n) and (n-1) % A(n) == 0:
    N.append(n)
  n += 2
  if n % 5 == 0:
    n += 2

print(sum(N))
