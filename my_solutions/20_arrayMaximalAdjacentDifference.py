"""
Author: Sikder Tahsin Al-Amin
Problem:
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""

def arrayMaximalAdjacentDifference(inputArray):
    diff=-999999
    for i in range(0,len(inputArray)-1):
        if abs(inputArray[i]-inputArray[i+1])>diff:
            diff = abs(inputArray[i]-inputArray[i+1])
    return diff
            

