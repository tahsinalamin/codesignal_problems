"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".
"""
def alphabeticShift(inputString):
    output=[]
    for i in range(len(list(inputString))):
        if inputString[i]=="z":
            output.append("a")
        else:
            output.append(chr(ord(inputString[i])+1))
    s=""
    for i in output:
        s=s+i
    return s
