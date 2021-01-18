"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
"""


def fileNaming(names):
    #uniquenames=set(names)
    #for i in range(len(uniquenames)):
     #   dic[i] = 0
        
    #print(dic)
    uniq = []
    for i in range(len(names)):
        if names[i] not in uniq:
            uniq.append(names[i])
        else:
            k = 1
            while True:
                if (names[i] + "(" + str(k) + ")") in uniq:
                    k += 1
                else:
                    uniq.append(names[i] + "(" + str(k) + ")")
                    break
    return uniq

names=["a(1)", 
 "a(6)", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a", 
 "a"]
print(fileNaming(names))
