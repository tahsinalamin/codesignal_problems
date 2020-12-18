"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;

"""

def isMAC48Address(inputString):
    s="ABCDEF0123456789-"
    p=[2,5,8,11,14]
    for i in inputString:
        if i not in s:
            return False
            
            
    for i in range(len(inputString)):
        if i not in p and inputString[i]=="-":
            return False
    if len(inputString)!=17:
        return False
            
    return True
    

