def isBeautifulString(inputString):
    d={}
    s="abcdefghijklmnopqrstuvwxyz"
    s=list(s)
    print(s)
    for i in range(len(inputString)):
        if inputString[i] in d:
            d[inputString[i]]+=1
        else:
            d[inputString[i]]=1

    dic = d.items()
            
    dic=sorted(dic)
    
    print(dic)
    for i in range(len(d)-1):
        #print(dic[i][1],dic[i+1][1])
        print(dic[i][0],s[i])
        if dic[i][0]!=s[i] or dic[i+1][0]!=s[i+1]:
            return False
        if int(dic[i][1])<int(dic[i+1][1]):
            return False
            
    return True
        
    
    
inputString = "bbbaacdafe"
print(isBeautifulString(inputString))

