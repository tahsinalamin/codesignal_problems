"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
"""

def evenDigitsOnly(n):
    while n!=0:
        r=n%10
        if r%2!=0:
            return False
            
        n=int(n/10)
    return True
    

