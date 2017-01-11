#Very crudely hacked together solution that doesn't take you all the way to the answer
numerators = [] #check out the problem to make sense of it at the end especially
denominators = []

for i in xrange(11,100):
	for j in xrange(10, i):
		numerators.append(str(j))
		denominators.append(str(i))

print numerators
print denominators

numers = []
denoms = []
simpN = []
simpD = []

for k in xrange(len(numerators)):
	if numerators[k][0] == denominators[k][0]:
		numers.append(numerators[k])
		denoms.append(denominators[k])
		simpN.append(numerators[k][1])
		simpD.append(denominators[k][1])
	elif numerators[k][1] in denominators[k][0]:
		numers.append(numerators[k])
		denoms.append(denominators[k])
		simpN.append(numerators[k][0])
		simpD.append(denominators[k][1])
	elif numerators[k][0] in denominators[k][1]:
		numers.append(numerators[k])
		denoms.append(denominators[k])
		simpN.append(numerators[k][1])
		simpD.append(denominators[k][0])
	elif numerators[k][1] in denominators[k][1]:
		numers.append(numerators[k])
		denoms.append(denominators[k])
		simpN.append(numerators[k][0])
		simpD.append(denominators[k][0])

print numers
print denoms
print simpN
print simpD

dcf = []
for n in xrange(len(numers)):
	if simpD[n] == '0':
		continue
	elif float(numers[n])/float(denoms[n]) == float(simpN[n])/float(simpD[n]) and float(numers[n])%float(simpN[n]) == 0:
		dcf.append(str(numers[n])+'/'+str(denoms[n]))
newdcf = []
for m in dcf:
	if m.endswith('0') == True:
		pass
	else:
		newdcf.append(m)
print newdcf
x = 16*26*19*49 
y = 64*65*95*98
print float(x) / float(y)