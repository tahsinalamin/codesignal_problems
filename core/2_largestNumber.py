"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.
"""

def largestNumber(n):
    largenumber=""
    while n!=0:
        largenumber+="9"
        n=n-1
        
    return int(largenumber)
