def inc(s):
	if len(s) < 2 : return True
	if s[0] <= s[1] : return inc(s[1:])
	return False

def dec(s):
	if len(s) < 2 : return True
	if s[0] >= s[1] : return dec(s[1:])
	return False

def bouncy(s) :
	return not (dec(s) or inc(s))

def count_b(n):
	count = 0
	for i in range(n+1):
		if bouncy(str(i)) : count += 1
	return count

i = 1000000
n = 1000000
b_count = 987048
b_count0 = 987048
lock = False
while True:
	p = b_count/n * 100
	p0 = b_count0/(n-1) * 100
	if p == 99 and p0 != 99:
		break
	if p > 99 :
		lock = False
		n -= i
	if p < 99 :
		if not lock:
			if i > 1:
				i //= 10
			lock = True
		n += i
	b_count = count_b(n)
	b_count0 = count_b(n-1)

print(n)