import time
def combinationCount(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def factorial(n):
    fact = 1;
    if n == 0:
        return fact
    else:
        for i in range(1, n + 1):
            fact *= i
        return fact
start = time.time()
count = 0
for n in range(1, 101):
    for r in range(1, 101):
        if combinationCount(n,r) > 1000000:
            count += 1
end = time.time()
print(count)
print(str(end - start) + " seconds")
