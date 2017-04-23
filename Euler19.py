from datetime import date, timedelta

d = date(1901, 1, 1)
delta = timedelta(hours=24)

count = 0

while d.year < 2001:
	if d.weekday() == 6 and d.day == 1:
		count += 1
	d = d + delta

print(count)