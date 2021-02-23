"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.
"""

def addTwoDigits(n):
    digits=[]
    while n!=0:
        r=n%10
        n=n//10
        digits.append(r) 
    
    return sum(digits)
