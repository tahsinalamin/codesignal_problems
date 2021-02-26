"""
in the given number n the kth bit from the right was initially set to 0, but its current value might be different. It's now up to you to write a function that will change the kth bit of n back to 0.

Example

For n = 37 and k = 3, the output should be
killKthBit(n, k) = 33.

3710 = 1001012 ~> 1000012 = 3310.
"""

def killKthBit(n, k):
    nbin = list(bin(n))
    nbin=nbin[2:]
    for i in range(0,len(nbin)):
        if i==len(nbin)-k:
            nbin[i]='0'
    st=""
    
    binstr = st.join(nbin)
    nint = int(binstr,2)
        
    return nint
