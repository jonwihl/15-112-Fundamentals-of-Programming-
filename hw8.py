
def getCourse(courseCatalog, courseNumber): #worked with rhmarques
	if type(courseCatalog) == str:
		if courseCatalog == courseNumber:
			return courseNumber
		elif courseCatalog == []:
			return None
	else:
		for school in range(len(courseCatalog)):
			getCourse(courseCatalog[school], courseNumber)
			if getCourse(courseCatalog[school], courseNumber) != None:
				return courseCatalog[0] + "." + getCourse(courseCatalog[school], courseNumber)

def flatten(L, newList = []):
	if L == []:
		return []
	for i in range(len(L)):
		if type(L[i]) == list:
			flatten(L[i], newList)
		else:
			newList.append(L[i])
	return newList

def isPrime(n, factor=2):
    if (n < 2):
		return False
    elif (factor*factor > n):
    	return True
    elif (n % factor == 0):
		return False
    else:
		return isPrime(n, factor+1)

def digitCount(n):
	if n == 0:
		return 0
	else:
		return 1 + digitCount(n // 10)

import os

def findLargestFileWrapper(path, largest = 0, largestPath = ""):
	if os.path.isdir(path) == True:
		for filename in os.listdir(path):
			newPath = path + "/" + filename
			if os.path.isdir(path) == False:
				currentPath = newPath
			else:
				currentPath = findLargestFileWrapper(newPath)
				if os.path.getsize(path) > largest:
					return currentPath
	else:
		if os.path.getsize(path) > largest:
			return path
			

def findLargestFile(path):
	return findLargestFileWrapper(path)


# removeDsStore.py
def removeDsStore(path):
    if (os.path.isdir(path) == False):
        if (path.endswith(".DS_Store")):
            os.remove(path)
    else:
        # recursive case: it's a folder
        for filename in os.listdir(path):
            removeDsStore(path + "/" + filename)

# sierpinksy-triangle.py

from Tkinter import *

def init(data):
    data.level = 0

def drawHFractal(canvas, x, y, size, level):
    # (x,y) is the lower-left corner of the triangle
    # size is the length of a side
    if (level == 0):
        canvas.create_line(x - size // 2, y - size // 2, x - size // 2, y + size // 2)
        canvas.create_line(x - size // 2, y, x + size // 2, y)
        canvas.create_line(x + size // 2, y - size // 2, x + size // 2, y + size // 2)
    else:
        drawHFractal(canvas, x - size // 2, y - size // 2, size/2, level-1)
        drawHFractal(canvas, x + size // 2, y - size // 2, size/2, level-1)
        drawHFractal(canvas, x - size // 2, y + size // 2, size/2, level-1)
        drawHFractal(canvas, x + size // 2, y + size // 2, size/2, level-1)
        drawHFractal(canvas, 250, 250, 250, level - 1)

def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

def redrawAll(canvas, data):
    drawHFractal(canvas, 250, 250, 250, data.level)
    canvas.create_text(250, 25,
                       text = "Level %d H-Fractal" % (data.level),
                       font = "Arial 26 bold")
    canvas.create_text(250, 50,
                       text = "Use arrows to change level",
                       font = "Arial 10")

def mousePressed(event, data): pass

def timerFired(data): pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
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


courseCatalog = ["CMU",["CIT",[ "ECE", "18-100", "18-202", "18-213" ],[ "BME", "42-101", "42-201" ],],["SCS",
                            [ "CS", 
                              ["Intro", "15-110", "15-112" ],
                              "15-122", "15-150", "15-213"
                            ],
                        ],
                        "99-307", "99-308"
                    ]

print(findLargestFile("sampleFiles/folderA"))