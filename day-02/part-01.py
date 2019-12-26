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

i = 0
while i in range(len(myList)) :
	# print(myList[i])
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
print(myList[0])