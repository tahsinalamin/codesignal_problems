"""
Determine if the given character is a digit or not.

Example

For symbol = '0', the output should be
isDigit(symbol) = true;
For symbol = '-', the output should be
isDigit(symbol) = false.
"""


def isDigit(symbol):
    digit="0123456789"
    if symbol in digit:
        return True
        
    return False

