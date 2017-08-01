A =[[1,-2,2],
    [2,-1,2],
    [2,-2,3]]

B =[[1,2,2],
    [2,1,2],
    [2,2,3]]

C =[[-1,2,2],
    [-2,1,2],
    [-2,2,3]]

def mult(x, y):
  z = [0, 0, 0]
  for i in range(3):
    for j in range(3):
      z[i] += (x[i][j] * y[j])
  return z

perims = {}
lim = 1500000

def count_perims(trip):
  global perims
  k = 1
  p = sum(map(lambda x: x*k, trip))
  if p > lim: return
  while p <= lim:
    if p in perims:
      perims[p] += 1
    else:
      perims[p] = 1
    k += 1
    p = sum(map(lambda x: x*k, trip))
  for i in [mult(x, trip) for x in (A,B,C)]:
    count_perims(i)

trip = [3, 4, 5]
count_perims(trip)
print(len([p for p in perims.values() if p == 1]))
