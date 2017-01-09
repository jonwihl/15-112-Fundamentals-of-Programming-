from random import *

def c1():
	if randint(0,100) <= 30:
		return 3
	else:
		return 0

def c2():
	if randint(0, 100) <= 75:
		return 5
	else:
		return 13

def c3():
	if randint(0, 100) <= 20:
		return(c1())
	else:
		return 0

def subway():
	time = 0
	time += c1()
	for i in range(5):
		time += c2()
	for i in range(5):
		time += c3()
	return time

def monteCarlo():
	trials = 500
	total = 0
	for i in range(trials):
		total += subway()
	print("Average time on subway %d" % (total / trials))

monteCarlo()