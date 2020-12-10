"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
"""

def longestDigitsPrefix(inputString):
    digits="1234567890"
    s=list(inputString)
    prefix=""
    for i in range(len(list(inputString))):
        if s[i] in list(digits):
            prefix+=s[i]
        else:
            break
            
    return prefix
