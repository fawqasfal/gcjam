from math import *
filen = 'B-large'
with open(filen + '.in') as inp:
	arrs = [[float(elem.strip('\n')) for elem in inp.next().split(' ')]for x in xrange(int(inp.next()))]
#arr = [case1, case2, case3...] where casen = [cost of cookie farm, increase in rate, tot needed]
ans = []
for arr in arrs:
	c = float(arr[0]) #cost of farm
	f = float(arr[1]) #increase in rate per farm
	x = float(arr[2]) #total cookies needed
	caseans = [x / 2.0]
	n = 1 
	"""n represents how much you would have to wait to be able to buy x cookies if you stopped buying farms at n farms.
	ex. : n = 0; x = 2000; then you need 1000 secs, or 2000 / 2.0, since 2.0 is your start rate.
	n = 1; c = 50; f = 10; x = 2000; 
	then you need 2000 / (2 + 10 * 1), or 2000 / 12 secs, to produce 2000 cookies at a rate of (2 + 10) cookies 
	per sec, seeing as 10 is your increase in rate per farm. then, add 50 / (2), or the time you had to wait to 
	get that farm at the speed of 2 cookies per second. 
	so, tot time to get x cookies with n farms, including the time to get to n farms with a start rate of 2 : 
	x / (2 + f * n) <- this represents how much time is needed to produce x cookies once you have n farms.
	c / (2 + i * f), loop from i = 0 to i = n, exclusive. this is the time needed to buy each farm at 
	2 + (i - 1) * f's rate, since youve bought i - 1 farms once you get to buying the ith farm.
	final answer : x / (2 + f * n) + sum([c / 2 + i *f) for i in xrange(n)])).
	try for all ns until you start seeing the time increasing.
	i noticed a trend that once time to get to x cookies and n farms increases, it doesnt stop increasing as n increases.
	buying more farms optimizes time until a point, at which case it increases indefinitely. once you start seeing it increasing, break the loop."""
	while True:
		caseans.append(x / (2 + f * n) + sum([c / (2 + i * f) for i in xrange(n)]))
		if caseans[n] > caseans[n- 1]:
			break
		n += 1
	ans += [caseans[len(caseans) - 1]]
print ans
ans = '\n'.join(["Case #%d: "%(x + 1) + str(ans[x]) for x in xrange(len(ans))])
with open(filen +'.out','w') as outp:
	outp.write(ans)