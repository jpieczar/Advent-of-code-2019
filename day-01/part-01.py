myFile = open("input.txt", 'r')
myList = []
for myLine in myFile:
	myLine = int(myLine.strip())
	myList.append((myLine // 3) - 2)
myFile.close()
myFile2 = open("output.txt", 'w')
sum = 0
for myLine in myList:
	sum += myLine
	myFile2.write(str(myLine) + '\n')
myFile2.close()
print(sum)