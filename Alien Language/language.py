import re

with open("A-large-practice.in",'r') as f:
	lines = f.read().split("\n")
w_size = int(lines[0].split(" ")[0]) #number of letters in a word
d_size = int(lines[0].split(" ")[1]) #number of words in the alien dictionary
dic = [] #dictionary
for i in range(1,d_size+1):
	dic.append(lines[i])

ans = "" #answer string to be written to output file
tot = 0 #total amount of possible words for any given list of tokens; reset to 0 for every test case
def skip(phrase): #checks to see if we can skip a word building off tokens that isn't in the dictionary to save time
	for word in dic:
		if phrase == word[:len(phrase)]:
			return False
	return True

def search(tokens, i, curr_word): #given a list of tokens, recursively search for all possibilities 
	if len(curr_word) == w_size: #base case
		global tot
		tot += 1 #implicit return; the function never visits the other possibilities

	elif tokens[i] != "(":
		curr_word += tokens[i]
		if not skip(curr_word):
			search(tokens, i+1, curr_word)
	
	else:
		end = tokens.find(")", i)
		for j in range(i+1, end):
			new_word = curr_word + tokens[j]
			if not skip(new_word):
				search(tokens, end+1, new_word)

for phrase in range(d_size+1, len(lines)):
	tot = 0
	search(lines[phrase],0,"")
	x = "Case #" + str(phrase - d_size) + ": " + str(tot) + "\n"
	print(x)
	ans += x

with open("A-large-practice.out", 'w') as outp:
	outp.write(ans)


