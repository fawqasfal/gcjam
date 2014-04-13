filen = 'A-small-attempt0'
allof = "Bad magician!"
noneof = "Volunteer cheated!"
with open(filen + '.in') as inp:
	tcases = inp.next()
	arr = []
	for case in xrange(int(tcases)):
		ans1 = inp.next()
		ans1 = int(ans1.strip('\n'))
		arr1 = [[int(elem.strip('\n')) for elem in inp.next().split(' ')] for x in xrange(4)]
		ans2 = int(inp.next().strip('\n'))
		arr2 = [[int(elem.strip('\n')) for elem in inp.next().split(' ')] for x in xrange(4)]
		finarr = [ans1, arr1, ans2, arr2]
		arr += [finarr]
#arr has testcases like this [t1, t2, t3...], where each tn is [ans1, [[row1],[row2],[row3],[row4]], ans2, [[row1],[row2],[row3],[row4]]]
ans = []
for test in arr:
	row1 = test[1][test[0] - 1]
	row2 = test[3][test[2] - 1]
	possans = [x for x in row1 if x in row2]
	if not len(possans):
		possans = [noneof]
	if len(possans) > 1:
		possans = [allof]
	ans.append(possans[0])
ans = '\n'.join(["Case #%d: "%(x + 1) + str(ans[x]) for x in xrange(len(ans))])
with open(filen +'.out','w') as outp:
	outp.write(ans)