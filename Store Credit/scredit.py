"""
You receive a credit C at a local store and would like to buy two items. You first walk 
through the store and create a list L of all available items. From this list you would like to 
buy two items that add up to the entire value of the credit. The solution you provide will 
consist of the two integers indicating the positions of the items in your list (smaller number first).
"""

"""
The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:
One line containing the value C, the amount of credit you have at the store.
One line containing the value I, the number of items in the store.
One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
Each test case will have exactly one solution.
"""

with open("A-large-practice.in",'r') as inp: 
	n = int(inp.next())
	#data is a 3d array : each case is a subarray like [C, I, [P1, P2, P3 ... PI]] for the Nth test case, where data[N] is the N-1th subarray
	data = [[int(inp.next()), int(inp.next())] + [inp.next().split()] for x in xrange(n) ]#crazy ass list comprehensions bro

"""
For each test case, output one line containing "Case #x: " 
followed by the indices of the two items whose price adds up to the store credit. The lower index should be output first.
"""
answer = ''
cnum = 0 #tracks which case you are at
#basic brute force O(n^2) algo : test each combo of pairs until you find an answer
for case in data:
	brk = False #set to true if you found the answer, such that if break is ever true you break out of the O(n^2) search loop
	cnum += 1 #adds 1 in the beginning instead of the end so that we start at Case 1 instead of Case 0
	answer += 'Case #%d: '%(cnum) 
	cred = case[0]
	#fnum, snum are indices of the items
	for fnum in xrange(case[1]):
		if brk:
			break
		for snum in xrange(case[1]):
			if snum == fnum: 
			"""you cant buy 2 of the same item -- if this is the same, skip to the next one. 
			you know the next one is not past the end of the list, because if it were, then you havent broken from the loop yet,
			then you havent found the answer yet, but youre past the end of the list, so there is no answer. but google promises 
			you that at least one answer exists. so you can be sure that you can at least find an answer at, or before the end of the list"""
				snum += 1
			if int(case[2][fnum]) + int(case[2][snum]) == cred:
				answer += str(fnum + 1) + " " + str(snum + 1)
				brk = True #if you found this case's answer, great just break! 
				break
	answer += '\n'
with open("A-large-practice.out", 'w') as outp:
	outp.write(answer)

