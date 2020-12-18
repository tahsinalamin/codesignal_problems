"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".
"""

def lineEncoding(s):
    freq=[]
    char=[]
    s=list(s)
    i=0
    while i<len(s):
        count=0
        j=i
        while s[j]==s[i]:
            count+=1
            j+=1
            if j>=len(s):
                break
            
        freq.append(count)
        char.append(s[i])
        i+=count
        
    encode=""
    for i in range(len(freq)):
        if freq[i]>1:
            encode+=str(freq[i])+char[i]
        else:
            encode+=char[i]
             
    return encode
    




s = "aabbbc"
print(lineEncoding(s))
