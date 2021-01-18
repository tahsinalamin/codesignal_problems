"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
"""

def digitsProduct(product):
    digits=[]
    if product ==0:
        return 10
    elif product<10:
        return product
    
    while product>1:
        for i in range(9,1,-1):
            if product % i == 0:
                product = product/i
                digits.append(i)
                break
        else:
            return -1
    
                
    s=""
    for i in sorted(digits):
        s+=str(i)
        
    
    return int(s)
