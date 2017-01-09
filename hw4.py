import tkinter
from tkinter import *

def lookAndSay(a): #creates looks and say list for number n
	result = []
	count = 1
	if a == []:
		return []
	previous = a[0]
	for i in range(1, len(a)):
		if a[i] == previous:
			count += 1
		else:
			result.append( (count, previous) ) #When a new number appears, add the number of occurences and the number to result
			count = 1
		previous = a[i]
	result.append((count, previous)) #Add the last element and its count
	return result

def inverseLookAndSay(a):
	result = []
	for i in range(len(a)):
		for j in range(a[i][0]):
			result.append((a[i][1]))
	return result

def solvesCryptarithm(puzzle, solution):
	word = ""
	result = []
	if len(solution) != 10: 
		return False
	for c in puzzle:
		if c != "+" and c != "=":
			if c not in solution:
				return False
			else:
				c = solution.index(c)
				word += str(c)
		elif c == "+" or c == "=":
			result.append(int(word))
			word = ""
	answer = int(word)
	return (addListElements(result) == answer)

def addListElements(lst):
	result = 0
	for i in range(len(lst)):
		result += lst[i]
	return result

def bestScrabbleScore(dictionary, letterScores, hand):
	highestScore = 0
	highScore = ""
	bestWord = ""
	hand = sorted(hand)
	for i in range(len(dictionary)):
		if hand == sorted(dictionary[i]):
			wordValue = wordScore(dictionary[i], letterScores)
			if wordValue >= highestScore:
				highScore += str(wordValue)
				bestWord += dictionary[i]
	if highestScore == 0:
		return None
	return (bestWord, highScore)


def wordScore(dictionary, letterScores):
	result = 0
	for c in dictionary:
		for i in range(len(c)):
			result += int(letterScores[(ord(c[i]) - 97)])
	return result

def drawCirclePattern(n):
	root = Tk()
	canvas = Canvas(root, width = 40 * n, height = 40 * n)
	drawBullseye(canvas, n)
	canvas.pack()
	root.mainloop()

def drawBullseye(canvas, n):
	circleRadius = 40
	color = ""
	for row in range(n):
		color = ""
		radius = 40 * row
		for col in range(n):
			color = ""
			if (col + row) % 4 == 0:
				color = "red"
			elif row % 3 == 0:
				color = "green"
			elif col % 2 == 1:
				color = "yellow"
			else:
				color = "blue"
			height = 40 * col
			canvas.create_oval(5 + height,  5 + radius,45 + height, 45 + radius, fill = color)
			while circleRadius > 1:
				circleRadius *= 2/3
				canvas.create_oval(5 + height + circleRadius,  5 + radius + circleRadius, 45 + height - circleRadius, 45 + radius - circleRadius, fill = color)
			circleRadius = 40

def runSimpleTortiseProgram(program, winWidth = 500, winHeight = 500):
	root = Tk()
	canvas = Canvas(root, winWidth, winHeight)
	lastWord = ""
	currentWord = ""
	currentLocationX = winWidth // 2
	currentLocationY = winHeight // 2
	for i in program:
		if i != "#":
			currentWord += i
		if i == " ":
			if checkCurrentWord(currentWord) == "move":
				lastWord = currentWord
				currentWord = ""
			if type(checkCurrentWord(currentWord)) == int:
				canvas.create_line(currentLocationX, currentLocationY, currentLocationX + int(currentWord), currentLocationY + int(currentWord))
	canvas.pack()
	root.mainloop()

def checkCurrentWord(s):
	ints = []
	directions = ["left", "right"]
	for i in range(500):
		ints += i
	if s == "move":
		return("move")
	elif int(s) in ints:
		result(int(s))
	elif s in directions:
		return(s)


def testLookAndSay():
	assert(lookAndSay([]) == [])
	assert(lookAndSay([1,1,1]) == [(3,1)])
	assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
	assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])

def testInverseLookAndSay():
	assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
	assert(inverseLookAndSay([]) == [])

