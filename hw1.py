import math 

def nearestBusStop(street):
	if street % 8 < 4 or street % 8 == 4:
		return street - street % 8
	else:
		return street - street % 8 + 8

def setKthDigit(n, k, d):
	num = n - n % 10 ** (k + 1)
	return num + d * 10 ** (k) + n % 10 ** k 

def cosineZerosCount(r):
	if abs(r) > math.pi/2 and r > 0:
		if abs(r) > math.pi:
			pi = (abs(r) / math.pi) // 1
			r -= pi * math.pi
			if r > math.pi/2:
				pi += 1
				return pi
			return pi
		else:
			return 1
	else:
		return 0

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
	a = totalTime
	b = -totalDistance
	c = -totalTime * (riverCurrent ** 2)
	x = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	v = x - riverCurrent
	return .5 * (totalDistance) / v

def rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2):
	if left2 <= left1 + width1 and top2 <= top1 + height1 and left2 + width2 >= left1 and top2 + height2 >= top1:
		return True
	return False

def threeLinesArea(m1, b1, m2, b2, m3, b3):
	if lineIntersection(m1, b1, m2, b2) == None or lineIntersection(m1, b1, m3, b3) == None or lineIntersection(m2, b2, m3, b3) == None:
		return 0
	(x1, y1) = lineIntersection(m1, b1, m2, b2)
	(x2, y2) = lineIntersection(m1, b1, m3, b3)
	(x3, y3) = lineIntersection(m2, b2, m3, b3)
	s1 = distance(x1, y1, x2, y2)
	s2 = distance(x2, y2, x3, y3)
	s3 = distance(x1, y1, x3, y3)
	return triangleArea(s1, s2, s3)

def lineIntersection(m1, b1, m2, b2):
	if m2 - m1 == 0 or (m2 -  m1 == 0 and b1 - b2 == 0):
		return None
	x = (b1 - b2) / (m2 - m1)
	y1 = m1*x + b1
	y2 = m2*x + b2
	if almostEqual(y1, y2) == True:
		return (x, y1)

def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def triangleArea(s1, s2, s3):
	s = (1/2)*(s1 + s2 + s3)
	return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d2 - d1) < epsilon)

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(2**0.5, 1, 1), 0.5))
    assert(almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed. (Add more tests to be more sure!)")

def testCosineZerosCount():
    print("Testing cosineZerosCount()...", end="")
    assert(type(cosineZerosCount(0)) == int)
    assert(cosineZerosCount(0) == 0)
    assert(cosineZerosCount(math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(math.pi/2 + 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 - 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 + 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 - 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 + 0.0001) == 3)
    assert(cosineZerosCount(-math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(-math.pi/2 + 0.0001) == 0)
    print("Passed. (Add more tests to be more sure!)")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed. (Add more tests to be more sure!)")


def testRiverCruiseUpstreamTime():
    print("Testing riverCruiseUpstreamTime()...", end="")
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.7888736053508778)) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.5))
    print("Passed. (Add more tests to be more sure!)")

def testRectanglesOverlap():
    print("Testing rectanglesOverlap()...", end="")
    assert(type(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)) == bool)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    print("Passed. (Add more tests to be more sure!)")