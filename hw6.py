import tkinter
from math import *
from tkinter import *

def isMagicSquare(a):
	assert(len(a) == len(a[0]))
	num = 0
	for i in range(len(a[0])):
		num += a[0][i]
	(rows, cols) = (len(a), len(a[0]))
	for row in range(rows):
		for col in range(cols):
			result = wordSearchFromCell(a, num, row, col)
			if (result == False):
				return False
	return True

def wordSearchFromCell(a, num, startRow, startCol):
    for dir in range(8):
        result = wordSearchFromCellInDirection(a, num,
                                               startRow, startCol, dir)
        if (result == False):
            return False

def wordSearchFromCellInDirection(a, num, startRow, startCol, dir):
    (rows, cols) = (len(a), len(a[0]))
    number = 0
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]    
    for i in range(len(a)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols)):
            return None
        else:
        	number += a[row][col]
    if number != num:
    	return False

def isKingsTour(board):
    onesPlace = findOne(board)
    currentPlace = adjacentCells(board, onesPlace[0], onesPlace[1])
    totalNumbers = len(board) * len(board[0])
    for i in range(len(board)):
        if not adjacentCells(board, currentPlace[0], currentPlace[1]):
            return False
    return True

    

def findOne(board):
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == 1:
				return(row, col)

def adjacentCells(board, startRow, startCol):
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]    
    row = startRow + drow
    col = startCol + dcol
    if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)):
        return None
    elif isNextNumber(board[startRow][startCol], board[row][col]):
    	return(True)
    return False

def isNextNumber(a, b):
    if b == a + 1:
        return True
    return False

def isLegalSudoku(board):
    boardLength = len(board)
    for i in range(boardLength):
        if isLegalRow(board, i) == False:
            return False
    for i in range(boardLength):
        if isLegalCol(board, i) == False:
            return False
    for i in range(boardLength):
        if isLegalBlock(board, i) == False:
            return False
    return True

def areLegalValues(values):
    num = len(values)
    lst = []
    for i in range(num + 1):
        lst.append(i)
    for c in values:
        if c not in lst or (c != 0 and values.count(c) != 1):
            return False
    return True

def isLegalRow(board, row):
    for i in range(len(board[row])):
        if areLegalValues(board[row]) == False:
            return False
    return True

def isLegalCol(board, col):
    result = []
    for i in range(len(board)):
        result.append(board[i][col])
    return areLegalValues(result)

def isLegalBlock(board, block):
    blockLength = int(sqrt(len(board)))
    result = []
    for i in range(blockLength):
        startingPos = block % blockLength * blockLength
        for j in range(blockLength):
            result.append(board[startingPos + i][startingPos + j])
    return areLegalValues(result)




######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#Place the manually graded solutions here

from tkinter import *

####################################
# Othello
####################################

def othelloInit(data):
    # load data.xyz as appropriate
    data.w_points = [(225,225,300,300), (300,300,375,375)]
    data.b_points = [(300,225,375,300), (225,300,300,375)]
    data.turn = "white"



def othelloMousePressed(event, data):
    squareWidth = data.width // 8
    squareX = (event.x // squareWidth) * squareWidth
    squareY = (event.y // squareWidth) * squareWidth
    if squareX >= 0 and squareY >= 0:
        if data.turn == "white":
            data.w_points += [(squareX, squareY, squareX + 1 * squareWidth, squareY + 1 * squareWidth)]
            a[squareX // squareWidth][squareY // squareWidth] = 0
            data.turn = "black"
        elif data.turn == "black":
            data.b_points += [(squareX, squareY, squareX + 1 * squareWidth, squareY + 1 * squareWidth)]
            data.turn = "white"
    # use event.char and event.keysym

    
def make2dList(rows, cols):
    board=[]
    for row in range(rows): a += [[0]*cols]
    return a

def hasMove(board, player):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            if (hasMoveFromCell(board, player, row, col)):
                return True
    return False

def hasMoveFromCell(board, player, startRow, startCol):
    (rows, cols) = (len(board), len(board[0]))
    if (board[startRow][startCol] != 0):
        return False
    for dir in range(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            return True
    return False

def hasMoveFromCellInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)):
            return False
        elif (board[row][col] == 0):
            # no blanks allowed in a sandwich!
            return False
        elif (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich
            i += 1
    return (i > 1)


def makeMove(board, player, startRow, startCol):
    # assumes the player has a legal move from this cell
    (rows, cols) = (len(board), len(board[0]))
    for dir in range(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            makeMoveInDirection(board, player, startRow, startCol, dir)
    board[startRow][startCol] = player

def makeMoveInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = startRow + i*drow
        col = startCol + i*dcol
        if (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich, so flip it!
            board[row][col] = player
            i += 1

def othelloTimerFired(data):
    pass

def othelloRedrawAll(canvas, data):
    squareWidth = data.width // 8
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = "green"
            else:
                color = "blue"
            canvas.create_rectangle(squareWidth * i, squareWidth * j, squareWidth * (i +1), squareWidth * (j + 1), fill = color)
    for i in range(len(data.w_points)):
        canvas.create_oval(data.w_points[i][0], data.w_points[i][1], data.w_points[i][2], data.w_points[i][3], fill = "white")
    for j in range(len(data.b_points)):
        canvas.create_oval(data.b_points[j][0], data.b_points[j][1], data.b_points[j][2], data.b_points[j][3], fill = "black")
####################################
# run function for Othello
####################################

def runOthello(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        othelloRedrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        othelloMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        othelloKeyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        othelloTimerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    othelloInit(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


