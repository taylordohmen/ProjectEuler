# counts the total number of letters in the string representations of 1-100 inclusive
# excludes spaces and hyphens and includes 'and' in, for instance, 'one hundred and six'

# letter counts of single digit numbers
ones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}

# letter counts of teen numbers including ten
teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}

# letter counts of twenty, thirty, fourty, ...
tens = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

total_letter_count = 0

def two_digit_count(x):
	x_int = int(x)
	if x_int < 20 and x_int > 9:
		return teens[x_int]
	elif x_int < 10:
		return ones[x_int]
	
	return tens[int(x[0])] + ones[int(x[1])]

for i in range(1, 1001):
	i_string = str(i)

	if len(i_string) == 1:
		total_letter_count += ones[i]
	elif len(i_string) == 2:
		total_letter_count += two_digit_count(i_string)
	elif len(i_string) == 3:
		tdc = two_digit_count(i_string[1:])
		# the + 7 is for 'hundred', the maybe +3 is for 'and'
		total_letter_count += ones[int(i_string[0])] + 7 + tdc + (3 if tdc > 0 else 0)

# for 'one thousand'
total_letter_count += 11

print(total_letter_count)