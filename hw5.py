import copy
import math
from math import *
import time

"""
1.)This function slow1 counts the elements in list a
2.)Runtime is O(n). The function loops through the entire list.
3.)
def slow1(a):
	return len(a)
4.)The big O of my funtion is O(1). It only runs len() once.

"""
def slow1(a):
    (b, c) = (copy.copy(a), 0)
    while (b != [ ]):
        b.pop()
        c += 1
    return c

"""
1.) Checks list a for duplicates. If there are duplicates it will return False
2.) Runtime is O(n**2). For each iteration of i (n times), the function checks it against n possibilities
3.) def slow2(a):
		return len(a) == len(set(a))
4.) O(1). The O(n) for len() is O(1) therefore the entire O(n) is O(1)

"""
def slow2(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(n):
            if (a[i] == a[j]):
                count += 1
    return (count == n)

"""
1.) Function calculates the number of differences between list a and list b.
2.) O(n). Loops through entire list.
3.) def slow3(a, b):
		return len(set(a) - set(b))
4.) O(1). Only one operation is done

"""
def slow3(a, b):
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    result = 0
    for c in b:
        if c not in a:
            result += 1
    return result 

"""
1.) Function returns the greatest difference between the values of a and b.
2.) O(n**2). For each value of c, the function checks it against every value in b.
3.) def slow4(a, b):
		return max(abs(max(a) - min(b)), abs(max(b) - min(a))
4.) O(n). The functions max() and min() both have a O(n)

"""
def slow4(a, b):
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    result = abs(a[0] - b[0])
    for c in a:
        for d in b:
            delta = abs(c - d)
            if (delta > result):
                result = delta
    return result

"""
1.) Finds the smallest difference between a and b.
2.) O(n**2). Checks each value of "c" n times.
3.) def slow4(a, b):


"""
def slow5(a, b):
    # Hint: this is a tricky one!  Even though it looks syntactically
    # almost identical to the previous problem, in fact the solution
    # is very different and more complicated.
    # You'll want to sort one of the lists,
    # and then use binary search over that sorted list (for each value in
    # the other list).  In fact, you should use bisect.bisect for this
    # (you can read about this function in the online Python documentation).
    # The bisect function returns the index i at which you would insert the
    # value to keep the list sorted (with a couple edge cases to consider, such
    # as if the value is less than or greater than all the values in the list, 
    # or if the value actually occurs in the list).
    # The rest is left to you...
    #
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    result = abs(a[0] - b[0])
    for c in a:
        for d in b:
            delta = abs(c - d)
            if (delta < result):
                result = delta
    return result


def invertDictionary(d): #inverts key : value pairs for dictionary d
	result = {}
	for key in d:
		if d[key] in result:
			result[d[key]].update(set([key])) #adds additional values if a key has more than one value
		else:
			result[d[key]] = set([key])
	return result


def friendsOfFriends(d):  #returns the friend of friends for dictionary d
	fof_dict = {key: [] for key in d}
	
	for person in d:
		for friends in d[person]:
			fof_dict[person] += d[friends]

	for person in fof_dict:					#removes person from their friend of friends
		for friend in fof_dict[person]:
			if person in fof_dict[person]:
				fof_dict[person].remove(person)

	for i in range(len(fof_dict)):
		for friend in fof_dict:  			 #removes original friends from friend of friends
			for name in fof_dict[friend]:
				if name in d[friend]:
					fof_dict[friend].remove(name)

	for friend in fof_dict:					#removes duplicates in persons friend of friends 
		for name in fof_dict[friend]:
			while fof_dict[friend].count(name) > 1:
				fof_dict[friend].remove(name)

	for key in fof_dict:
		fof_dict[key] = set(fof_dict[key])

	return fof_dict	

def largestSumOfPairs(a): #takes list of integers and returns the largest sum
	if len(a) <= 1:
		return None
	largestNumber = max(a)
	a.remove(largestNumber)
	secondLargest = max(a)
	return largestNumber + secondLargest

def containsPythagoreanTriple(a): #takes list of integers and checks if there is a pythagorian triplet in the list
	newList = set()
	for i in range(len(a)):  #creates new list containing the squares of each integer
		newList.add(a[i] ** 2)
	for i in a:
		for j in a:
			if (i ** 2 + j ** 2) in newList: #applies a ** 2 + b ** 2 == c
				return True
	return False

#################################################
# MergeSort - 4.19616699219e-05
# MergeSortWithOneAuxList - 4.50611114502e-05
#
# Merge sort with one aux list was slower in the 
# end
#################################################

def merge(a, start1, start2, end, aux):
    index1 = start1
    index2 = start2
    length = end - start1
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
    	a[i] = aux[i - start1]

def mergeSortWithOneAuxList(a):
    start = time.time()
    n = len(a)
    step = 1
    aux = [None] * n
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(a, start1, start2, end, aux)
        step *= 2
    end = time.time()
    return a

def mergeThreeWay(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def threeWayMergeSort(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 3*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 3*step, n)
            mergeThreeWay(a, start1, start2, end)
        step *= 3
    return a

def testInvertDictionary():
	assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == {2:set([1]), 3:set([2,5]), 4:set([3])})
	assert(invertDictionary({2:1, 5:3, 7:2, 3:2}) == {1: {2}, 2: {3, 7}, 3: {5}})
	assert(invertDictionary({}) == {})

def testLaregestSumOfPairs():
	assert(largestSumOfPairs([12345678, 12345679, 12345680, 12345681, 12345682]) == 24691363)
	assert(largestSumOfPairs([8,4,2,8]) == 16)
	assert(largestSumOfPairs([]) == None)
	assert(largestSumOfPairs([1]) == None)

def testContainsPythagoranTriple():
	assert(containsPythagoreanTriple([1,3,4,2,5,1,4]) == True)
	assert(containsPythagoreanTriple([1,4,2,5,1,4]) == False)
	assert((containsPythagoreanTriple([5,12,13]) == True))

def testMergeSortWithOneAuxList():
	assert(mergeSortWithOneAuxList([2,4,6,1,3,1342,23]) == [1, 2, 3, 4, 6, 23, 1342])
	assert(mergeSortWithOneAuxList([]) == [])

def testFriendsOFriends():
	assert(friendsOfFriends({'bam-bam': set(), 'fred': {'bam-bam', 'betty', 'barney', 'wilma'}, 'barney': set(), 'dino': set(), 'betty': set(), 'wilma': {'dino', 'fred', 'betty'}}) 
		== {'bam-bam': set(), 'fred': {'dino'}, 'barney': set(), 'dino': set(), 'betty': set(), 'wilma': {'bam-bam', 'barney'}})
	assert(friendsOfFriends({'B': {'C', 'A', 'D', 'E'}, 'C': set(), 'A': {'B', 'F', 'D'}, 'F': {'D'}, 'D': {'B', 'F', 'E'}, 'E': {'C', 'D'}})
		== {'B': {'F'}, 'C': set(), 'A': {'C', 'E'}, 'F': {'B', 'E'}, 'D': {'C', 'A'}, 'E': {'B', 'F'}})



