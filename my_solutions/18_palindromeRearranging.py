"""
Author: Sikder Tahsin Al Amin
Problem:
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

"""
from collections import Counter
def palindromeRearranging(inputString):
    res = Counter(inputString) #frequency of characters
    #print(res.values())
    odd = 0
    for i in res.values(): 
        if i%2!=0:
            odd+=1
    if odd>1:
        return False
    return True

