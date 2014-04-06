def bconvert(num, base):
	"""converts a num of base base to a num of base 10. assumes num can be represented in base base --i.e. base > num's biggest digit.
	the num is in list form with each elem as a digit.""" 
	#multiplies each digit by base^length of ndigits - index of digit, giving back its base 10 form. sums the whole thing up for the final int answer
	return sum([int(num[x]) * base ** (len(num) - (x + 1)) for x in xrange(len(num))]) 
with open('A-large-practice.in') as inp:
	cases = [inp.next().strip('\n') for x in xrange(int(inp.next()))]
unqs = [] #will be 2d arr of unique characters per case, so that there is a one-to-one correspondence between letters and nums
for case in cases:
	unq = []
	unq += (let for let in case if let not in unq)
	unqs += [unq]
"""this next line turns unqs into a 2d array of dicts, where each dict is a case's correspondence between letters (keys) and that letter's
corresponding number (values). the formula for turning letter into value goes like this:
	StringsUniqueChars = Char1Char2Char3Char4, values : Char1 = 1, Char2 = 0, Char3 = 2... etc., etc., or 
	string = 1023....
smallest numbers in the largest index -> largest numbers in the smallest index, makes for the smallest number. the reason we don't just
start at 0 is because google says 01234.... numbers are disallowed. the aliens drop the first zero!
unless the string length is 1, in which case we can say the number is just 0. 
The easiest way to this in code is 
CharVal = IndexOfCharInString if Index > 1, otherwise CharVal = -1  * IndexOfCharInString + 1, which swaps 0 with 1 and vica-versa."""
unqs = [{x: unq.index(x) if unq.index(x) > 1 else (-1 * unq.index(x) + 1) for x in unq} for unq in unqs]


ans = []
for case in xrange(len(cases)):
	thisunq = unqs[case]
	thisans = [str(thisunq[let]) for let in cases[case]]
	#will hold base10 representation of this case's smallest number. right now holds base-N rep of smallest number... see next comment for more"
	thisans = str(bconvert(thisans, len(thisunq) if len(thisunq) > 1 else 2)) 
	"""the base of the number should be the smallest base possible for the smallest base10 rep possible -- the length of this case's unique values 
	is ThisDict'sMaxCharValue + 1, so a dict of length 3 has a largest number 2, which can fit in base 3 minimum.
	 minimum base overall is base 2, so we have the conditional at the end to make sure 1111111 gets interpreted as base2, not base1."""
	ans.append(thisans)
ans = '\n'.join(["Case #%d: "%(x + 1) + ans[x] for x in xrange(len(ans))])
with open('A-large-practice.out', 'w') as outp:
	outp.write(ans)
