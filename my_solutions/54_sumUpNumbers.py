"""
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.
"""

def sumUpNumbers(inputString):
    digits=list("1234567890")
    l=inputString.split(" ")
    numbers=[]
    for i in range(len(l)):
        flag=""
        tmp=list(l[i])
        for j in tmp:
            if j in digits:
                flag+=j
            else:
                if len(flag)>=1:
                    numbers.append(int(flag)) 
                    flag=""
                

        if len(flag)>=1:
            numbers.append(int(flag)) 
    return sum(numbers)    
                
    
    

