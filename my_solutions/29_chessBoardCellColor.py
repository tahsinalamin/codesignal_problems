"""
Given two cells on the standard chess board, determine whether they have the same color or not.

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.
"""


def chessBoardCellColor(cell1, cell2):
    d={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    c1=list(cell1)
    c2=list(cell2)
    
    #for i in range(0,len(c1)):
    col1=d[c1[0]]
    row1=int(c1[1])
        
    col2=d[c2[0]]
    row2=int(c2[1])
     
    #cellval1=val11*val12
    #cellval2=val21*val22
    
    color1=1
    color2=1
    
    if col1%2!=0 and row1%2!=0:
        color1=0
        
    if col1%2==0 and row1%2==0:
        color1=0
    
    if col2%2!=0 and row2%2!=0:
        color2=0
        
    if col2%2==0 and row2%2==0:
        color2=0
    return color1==color2
