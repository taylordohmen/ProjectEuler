# Solution based on the Stern-Brocot tree.

from collections import deque

D = 12000

count = 0
queue = deque([((1,3), (2,5), (1,2))])

while queue:
    trip = queue.popleft()
    x, y, z = trip
    a, b = x
    c, d = y
    e, f = z
    if d <= D:
        count = count + 1
        left = ((a, b), (a+c, b+d), (c, d))
        right = ((c, d), (c+e, d+f), (e, f))
        queue.append(left)
        queue.append(right)

print(count)