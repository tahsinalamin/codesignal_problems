"""
Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)

If there are several possible answers, output the smallest one.
"""

def absoluteValuesSumMinimization(a):
    minimum=999999999
    x=-1
    for i in range(0,len(a)):
        currentMin=0
        for j in range(0,len(a)):
            if i!=j:
                currentMin+=abs(a[i]-a[j])
            if currentMin>minimum:
                break
        if currentMin<minimum:
            minimum=currentMin
            x=a[i]
    return x    

