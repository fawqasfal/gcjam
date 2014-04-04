with open("B-large-practice.in",'r') as inp:
	strs = [inp.next().split() for x in xrange(int(inp.next()))] 
	#strs is now 2d arr where each subarray is a case with each word as an elem

strs = [st[::-1] for st in strs] #reverse the order of words in each subarray
strs = ["Case #%d: "%(st + 1) + ' '.join(strs[st]) for st in xrange(len(strs))] #append Case #N to the joined string of the rev'd words, making it 1d
strs = '\n'.join(strs) #join the 1d list on \ns, turning the whole thing into a string 
"""the whole problem as one line : 
strs = '\n'.join("Case #%d: "%(st + 1) + ' '.join(strs[st][::-1]) for st in xrange(len(strs)))"""
with open("B-large-practice.out",'w') as outp:	
	outp.write(strs)