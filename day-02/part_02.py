def intcode(noun, verb):
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

def this():
	l = 0
	k = 0
	a = 0
	b = 19690720
	while l in range(100):
		k = 0
		while k in range(100):
			a = intcode(l, k)
			if a == b:
				print(l)
				print(k)
				return
			k += 1
		l += 1
	return

this()

