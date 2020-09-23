"""
Author: Sikder Tahsin Al-Amin
wo arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.
For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.
"""
def areSimilar(a, b):
    swap=0
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            swap +=1
            
    if swap <=2 and sorted(a)==sorted(b):
        return True
    return False
