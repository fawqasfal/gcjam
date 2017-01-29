inp = []
with open("B-large-practice.in",'r') as f: 
	lines = f.read().split("\n")
lines = lines[1:] #no need for the number of test cases, as we are reading to EOF 
t = 0 #line index
k = 1 #number of test cases 
ans_arr  = [] #final array of answer

def satisfaction(p, m): #p contains the preference set, m contains the array of malted beverages
	for c in p:
		if c[0] == 0 or (len(c) == 3 and c[2] == 1 and c[1] not in m): 
		#if this customer has no valid preferences or has only one malted preference that is unmalted
			return [False,c] #return False and the unsatisfied custoemr
	return [True,0]

while t < len(lines):
	ans = "Case #" + str(k) + ": " #were on the kth case here
	a_arr = [] #contains the beverages that must be malted 
	n = int(lines[t]) #number of flavors
	m = int(lines[t+1]) #number of customers
	p = [] #"preferences"; a list of lists; each list is a customer preference
	for j in range(2,m+2):
		c = [int(x) for x in lines[t+j].split(" ")]
		p.append(c)
	possible = True #if we uncover that this case is impossible
	
	satisfied = satisfaction(p,a_arr)
	while not satisfied[0]:
		unsatisfied = satisfied[1] #the unsatisfied customer
		if unsatisfied[0] == 0:
			possible = False #we have exhausted all possibilities of c's unmalted prefs & it has left us with an impossible situation
			break
		a_arr.append(unsatisfied[1])
		for c in p:
			for i in range(1,len(c),2): #the odd elements of c possess the flavor # of c's preferences
				if c[i] == unsatisfied[1] and c[i+1] == 0: #this is our malted flavor in c's unmalted preferences
					c[0] -= 1
					del c[i] #get rid of the flavor that must be unmalted 
					del c[i] #get rid of the 0 after that flavor's unmaltedness; it's index has been pushed down from i+1 to i
					break #we've already found the necessary flavor, no need to keep looking in this customer
		satisfied = satisfaction(p,a_arr)

	if not possible:
		ans += "IMPOSSIBLE\n"
	else:
		for i in range(n):
			if (i+1) in a_arr:
				ans+= "1 "
			else:
				ans+= "0 "
		ans+= "\n"
	ans_arr.append(ans)
	t += m + 2
	k += 1

with open("B-large-practice.out", 'w') as outp:
	for ans in ans_arr:
		outp.write(ans)


