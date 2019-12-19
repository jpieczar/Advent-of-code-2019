myFile = open("input.txt", 'r')
myList = []
sum = 0
for myLine in myFile:
	num = 0
	myLine = int(myLine.strip())
	while myLine > 0:
		myLine = ((myLine // 3) - 2)
		if (myLine > 0):
			num += myLine
	sum += num
myFile.close()
print(sum)