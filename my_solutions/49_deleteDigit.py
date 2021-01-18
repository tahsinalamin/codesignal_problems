def deleteDigit(n):
    s=list(str(n))
    
    minimum=999
    pos=-1
    l=[]
    for i in range(len(s)):
        tmp=s[:i]+s[i+1:]
        print(tmp)
        d=""
        for j in tmp:
            d+=j
        print(d)
        l.append(int(d))
        
        
    return max(l)
    
n = 152
print(deleteDigit(n))
