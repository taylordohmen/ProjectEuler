def A(n):
  r = 1111
  rep_len = 4
  r_mod = r % n
  while r_mod != 0:
    r = r * 100 + 11
    r_mod = ((r_mod * (100%n) % n) + (11 % n)) % n
    rep_len += 2
  return rep_len

lim = 1000000
n = lim + 3
a = A(3)
while True:
  n += 2
  while n % 5 == 0:
    n += 2
  a = A(n)
  if a > lim:
    break

print(n, a)
