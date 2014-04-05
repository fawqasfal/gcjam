alphdict = dict({' ': 0}.items() + {chr(key): ((key - 97) / 3) + 2 for key in xrange(97, 123)}.items()) 
#Using dict comprehension magic, this makes a dict with ' ' and lowercase letters 'a..z' as keys, and their respective T9 num mappings as vals
alphdict['s'] = 7
alphdict['v'] = 8
alphdict['y'] = 9
alphdict['z'] = 9 
#formula above works by assinging 3 letters per num ... real T9 has some special cases/exceptions cause the alphabet is unfortunately not div by 3

"""2d arr with indices being the T9 num vals and the arrs being the T9 letters on that num val
alpharr is used to figure out exactly how many times you need to press a key in order to achieve the letter;
for example, alphdict 'b' tells us you need to press 2 for 'b', but only alpharr can tell us how many times to press 2 in order to get 'b'"""
alpharr = [[' '],[]] + [[chr(num) for num in xrange(t9, t9 + 3)] for t9 in xrange(97,122,3)]
alpharr[7] += 's'
alpharr[8] = ['t','u','v']
alpharr[9] = ['w','x','y','z']
alpharr.pop(10)

with open('C-large-practice.in', 'r') as inp:
	inplets = [inp.next().strip('\n') for case in xrange(int(inp.next()))]

def toT9(case):
	#solve any one case in just one line:
	#ans = ''.join([(' ' if let > 0 and alphdict[case[let - 1]] == alphdict[case[let]] else '') + str(alphdict[case[let]]) * (alpharr[alphdict[case[let]]].index(case[let]) + 1) for let in xrange(len(case))])	
	ans = ''
	for let in xrange(len(case)):
		thisnum = alphdict[case[let]]
		if let > 0 and alphdict[case[let - 1]] == thisnum: #see if you have to press the same number again, in which case pause
			ans += ' '
		ans += str(thisnum) * (alpharr[thisnum].index(case[let]) + 1) #index of let in alpharr + 1 tells us how many times you need to press
		#ex.: 'b' is the 1st index on the 2 button, so we need to press 2 twice to get 'b'	
	return ans

rightans = [toT9(case) for case in inplets]
rightans = '\n'.join(["Case #%d: "%(x + 1) + rightans[x] for x in xrange(len(rightans))])
with open('C-large-practice.out', 'w') as outp:
	outp.write(rightans)
