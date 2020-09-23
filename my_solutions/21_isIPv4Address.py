"""
Author: Sikder Tahsin Al Amin
Problem:
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
Given a string, find out if it satisfies the IPv4 address naming rules.

Example
For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.
"""

def isIPv4Address(inputString):
    ip=inputString.split(".")
    if len(ip)!=4:
        return False
    #print(ip)
    for i in ip:
        if len(i)>1 and i[0]=="0":
            return False
            
        if i.isdigit()==False or i=="00":
            return False          
        elif  i=="" or int(i)>255:
            return False
    return True
