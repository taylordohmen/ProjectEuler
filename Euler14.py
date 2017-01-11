#Sad, inefficient 26 second long solution :(
def CollatzSequenceLength(x):
	nums = [x]
	while nums[len(nums)-1] != 1:
		if nums[len(nums)-1] % 2 == 0:
			nums.append(nums[len(nums)-1] / 2)
		else:
			nums.append((3*nums[len(nums)-1]) + 1)
	return (len(nums),x)
print CollatzSequenceLength(13)
def longestSequence(n):
	print (n/2) + 1
	lengths = []
	for i in range((n/2) + 1,n,2):
		lengths.append(CollatzSequenceLength(i)[0])
	print max(lengths)
	print lengths.index(max(lengths)) *2 + (n/2) + 1
longestSequence(1000000)