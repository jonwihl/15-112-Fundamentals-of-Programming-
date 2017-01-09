import math

def sumOfSquaresOfDigits(n):
	total = 0
	while n > 0:
		total += (n % 10) ** 2
		n //= 10
	return total

def isHappyNumber(n):
	if n < 0:
		return False
	for i in range(200):
		n = sumOfSquaresOfDigits(n)
		if n == 1:
			return True
	return False

def nthHappyNumber(n):
	count = 0
	num = 2
	while count < n:
		if isHappyNumber(num) == True:
			count += 1
		num += 1
	return num - 1

def nthHappyPrime(n):
	count = 0
	num = 2
	while count <= n:
		if isHappyNumber(num) and fasterIsPrime(num):
			count += 1
		num += 1
	return num - 1

def kaprekarNumber(n):
	count = 1
	y = n ** 2
	if n == 1:
		return n
	while y // 10 ** count > 0:
		if y % 10 ** count + y // 10 ** count == n:
			return True
		count += 1
	return False

def nearestKaprekarNumber(n):
	num = 0
	test = 0
	while n > num:
		num = nthKaprekarNumber(test)
		test += 1
	if num - n >= n - nthKaprekarNumber(test - 2):
		return nthKaprekarNumber(test - 2)
	else:
		return num

def nthKaprekarNumber(n):
	count = 0
	num = 0
	while count <= n:
		if kaprekarNumber(num) == True:
			count += 1
		num += 1
	return num - 1


def nthCarolPrime(n):
	test = 0
	count = 0
	while count <= n:
		if fasterIsPrime((2**(test) - 1)**2 - 2):
			count += 1
		test += 1
	return ((2**(test - 1) - 1)**2 - 2)

def carrylessAdd(x, y):
	count = 0
	total = 0
	while x > 0 or y > 0:
		total += ((x + y) % 10) * 10 ** count
		count += 1
		y //= 10
		x //= 10
	return total

def carrylessMultiply(x, y):
	count = 0
	total = 0
	orig = y
	temp = 0
	while x > 0:
		print(x)
		while y > 0:
			total += ((x * y) % 10) * 10 ** count
			count += 1
			y //= 10
			print(total)
		y = orig	
		count -= 1
		x //= 10
	return total

def f1(x):
	return math.sqrt(x - 1)

def f2(x):
	return 2 * x ** 2

def h(f, x): 		#takes function f and evaluates it at x
	return f(x)

def f3(x):
	return math.cos(x)

def integral(f, a, b, N): #finds trapeziodal integral of f from a to b
	total = 0
	deltaX = (b - a) / N
	i = a
	while i <= b:
		if i != a and i != b:
			total += 2 * h(f, i)
		else:
			total += h(f, i)
		i += deltaX
	print(i - deltaX)
	return round((deltaX / 2) * total)

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d2 - d1) < epsilon)


def fasterIsPrime(n): # taken from cs.cmu.edu
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True


def testSumOfSquaresOfDigits():
	print("Running Test....")
	assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
	assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
	assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29
	print("Test Passed")

def testIsHappyNumber():
	assert(isHappyNumber(-7) == False)
	assert(isHappyNumber(1) == True)
	assert(isHappyNumber(2) == False)
	assert(isHappyNumber(97) == True)
	assert(isHappyNumber(98) == False)
	assert(isHappyNumber(404) == True)
	assert(isHappyNumber(405) == False)

def testNthHappyNumber():
	assert(nthHappyNumber(0) == 1)
	assert(nthHappyNumber(1) == 7)
	assert(nthHappyNumber(2) == 10)
	assert(nthHappyNumber(3) == 13)
	assert(nthHappyNumber(4) == 19)
	assert(nthHappyNumber(5) == 23)
	assert(nthHappyNumber(6) == 28)
	assert(nthHappyNumber(7) == 31)
