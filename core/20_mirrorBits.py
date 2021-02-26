"""
Reverse the order of the bits in a given integer.

Example

For a = 97, the output should be
mirrorBits(a) = 67.

97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.
"""

def mirrorBits(a):
    abin = bin(a)
    alist = list(abin)
    alist = alist[2:]
    mbin = alist[::-1]
    mstr =""
    mstr = mstr.join(mbin)
    return int(mstr,2)
a = 97
print(mirrorBits(a))
