inp = []
with open("A-large-practice.in",'r') as f: 
	lines = f.read().split("\n")
	for line in range(len(lines)): 
		if (line-1) % 3 == 0:
			x = [int(x1) for x1 in lines[line+1].split()]
			x.sort()
			y = [int(y1) for y1 in lines[line+2].split()]			
			y = sorted(y, reverse=True)
			curr = 0
			for elem in range(len(x)):
				curr += x[elem]*y[elem]
			inp.append(curr)
with open("A-large-practice.out", 'w') as outp:
	for size in range(len(inp)):
		outp.write("Case #" + str(size + 1) + ": " + str(inp[size]) + "\n")
"""
The input is represented in an array of arrays. Each array holds a test case : The first element holds the N-vector representing x,
the second element holds the N-vector representing y. The algorithm simply sorts X and reverse sorts Y. This way, the biggest values of
X are increased by the smallest amounts of Y, and the smallest amounts in X get magnified with the largest numbers in Y."""