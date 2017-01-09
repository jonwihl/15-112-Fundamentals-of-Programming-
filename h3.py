import math

def condenseMessage(s):
	result = ""
	for i in range(len(s)):
		if s[i] != " ":
			result += s[i]
	return(result)

def condensePattern(s):
	result = ""
	start = 0
	end = len(s)
	if s[0] == "\n":
		start = 1
	if s[len(s) - 1] == "\n":
		end = len(s) - 1
	result += s[start:end]
	return result

def patternedMessage(message, pattern):
	if len(message) == 0 or len(pattern) == 0:
		return ""
	result = ""
	message = condenseMessage(message)
	pattern = condensePattern(pattern)
	count = 0
	for i in pattern:
		if count == len(message):
			count = 0
		if i != " " and i != "\n":
			result += message[count]
			count += 1
		elif i == " ":
			result += " "
		elif i == "\n":
			result += "\n"
	return(result)

def encodeRightLeftCipher(message, rows):
	col = math.ceil(len(message) / rows)
	encodedMessage = encode1(message, rows)
	return(str(rows) + readEncodedMessage(encodedMessage, col))

def encode1(message, rows):
	cols = math.ceil(len(message) / rows)
	result = ""
	count = 0
	counter = 0
	ascii_lower = "zyxwvutsrqponmlkjihgfedcba"
	for i in range(rows):
		count = 0
		for j in range(cols + 1):
			if i + (rows * j) < len(message):
				result += message[i + (rows * j)]
				count += 1
		if count < cols:
			result += ascii_lower[counter]
			counter += 1
	return(result)

def readEncodedMessage(message, rows):
	result = ""
	i = 0
	while i < len(message):
		if isOdd(i / rows):
			result += message[i + (rows - 1):i-1:-1]
		else:
			result += message[i:i + rows]
		i += rows
	return result

def isOdd(num):
	if num % 2 != 0:
		return True
	return False

def decodeRightLeftCipher(encodedMessage):
	result = ""
	cipherText = buildRightLeftCipher(encodedMessage)
	row = int(cipherText[1])
	col = math.ceil(len(encodedMessage) / row) - 1
	text = cipherText[0]
	for i in range(col):
		result += text[i:len(text):col]
	return(result.strip())


def buildRightLeftCipher(encodedMessage):
	result = ""
	ascii_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	ascii_lower = "zyxwvutsrqponmlkjihgfedcba"
	decodedMessage = decode(encodedMessage)
	rows = int(findInt(encodedMessage))
	for c in decodedMessage:
		if c in ascii_upper:
			result += c
		elif c in ascii_lower:
			result += " "
	return (result, rows)


def decode(encodedMessage):
	rows = int(findInt(encodedMessage))
	col = math.ceil(len(encodedMessage) / rows)
	result = ""
	encodedMessage = encodedMessage[digitCount(rows):]
	print(encodedMessage)
	i = 0
	count = 0
	while i < len(encodedMessage) - 1:
		if isOdd(count):
			result += stringReverse(encodedMessage[i:i + col - 1])
		else:
			result += encodedMessage[i:i + col - 1]
		i += col - 1
		count += 1
	return(result)

def findInt(s):
	ascii_int = "0123456789"
	result = ""
	for c in s:
		if c in ascii_int:
			result += c
	return result

def digitCount(n):
	count = 0
	while n > 0:
		n //= 10
		count += 1
	return count


def stringReverse(s):
	return s[::-1]

def bestStudentAndAvg(gradebook):
	gradebook = createAvg(gradebook)
	bestSoFar = -1000
	num = ""
	name = ""
	result = ""
	ascii_int = "0123456789-"
	ascii_lower = "zyxwvutsrqponmlkjihgfedcba"
	for c in gradebook:
		if c == "\n":
			num = intToString(num)
			if num >= bestSoFar:
				bestSoFar = num
				result = ""
				result += name + ":" + str(num)
			num = ""
			name = ""
		elif c != ":" and c in ascii_lower:
			name += c
		else:
			if c in ascii_int:
				num += c
	return(result)


def createAvg(gradebook):
	gradebook = cleanGradebook(gradebook)
	result = ""
	newPerson = ""
	grade = ""
	avgGrade = 0
	count = 0
	ascii_lower = "zyxwvutsrqponmlkjihgfedcba"
	ascii_int = "0123456789-"
	for c in gradebook:
		if c == "\n":
			avgGrade += intToString(grade)
			result += newPerson + ":" + str(avgGrade // count) + "\n" 
			newPerson = ""
			grade = ""
			avgGrade = 0
			count = 0
		elif (c != "," or "\n") and c in ascii_lower:
			newPerson += c
		else:
			if c in ascii_int:
				grade += c
			elif c == ",":
				avgGrade += intToString(grade)
				grade = ""
				count += 1
	return(result)

def cleanGradebook(gradebook):
	result = ""
	newBook = gradebook.splitlines()
	for c in newBook:
		if c != "" and c[0] != "#":
			result += c + "\n"
	return result
	
def intToString(num):
	count = 0
	result = 0
	for i in range(1, len(num) + 1):
		if num[-i] != "-":
			result += int(num[-i]) * 10 ** count
			count += 1
		else:
			result *= -1
	return result