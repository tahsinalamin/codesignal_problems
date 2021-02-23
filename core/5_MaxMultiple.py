"""
Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.

Example

For divisor = 3 and bound = 10, the output should be
maxMultiple(divisor, bound) = 9.
"""

def maxMultiple(divisor, bound):
    if bound<0:
        return 0
    while bound!=0:
        if bound%divisor==0:
            return bound
        bound=bound-1
        
    return bound
