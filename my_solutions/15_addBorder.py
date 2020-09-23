"""
Author: Sikder Tahsin Al-Amin
Problem:
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
Example:
For
picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
def addBorder(picture):
    h=len(picture) #height of the rectangle
    w=len(picture[0]) #width of the rectangle
    picBorder=[]
    
    picBorder.append("*"*(w+2))#first row
    for i in picture:
        picBorder.append("*"+i+"*")
    picBorder.append("*"*(w+2)) #last row
    
    return picBorder
