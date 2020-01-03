myFile = open("input.txt", 'r')
myList2 = []
for myLine in myFile:
	myLine = myLine.strip()
	myLine = myLine.split(',')
	myList2.append(myLine)
myFile.close()
myList = []
for j in myList2[0]:
	myList.append(int(j))

# The actual programme now...

def intcode(noun, verb):
	myList[1] = int(noun)
	myList[2] = int(verb)
	i = 0
	while i in range(len(myList)) :
		if myList[i] == 99:
			break
		elif myList[i] == 1:
			myList[myList[i + 3]] = myList[myList[i + 1]] + myList[myList[i + 2]]
			i += 4
		elif myList[i] == 2:
			myList[myList[i + 3]] = myList[myList[i + 1]] * myList[myList[i + 2]]
			i += 4
		else:
			i += 1
	return (myList[0])

noun = input("Noun: ")
verb = input("Verb: ")
print(intcode(noun, verb))

# 1969 - 07 - 20