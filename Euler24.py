from itertools import permutations
def millionthPerm(x,n):
	perms = list(permutations(x))
	return perms[n]
print millionthPerm((0,1,2,3,4,5,6,7,8,9),999999)