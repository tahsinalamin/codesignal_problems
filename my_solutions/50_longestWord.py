"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
"""

def longestWord(text):
    s="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    l=text.split(" ")
    maxLen=-999
    maxStr=""
    for i in range(len(l)):
        tmp=""
        for j in l[i]:
            if j in s:
                tmp+=j
        if len(tmp)>maxLen:
            maxLen=len(tmp)
            maxStr=tmp
            
    return maxStr
