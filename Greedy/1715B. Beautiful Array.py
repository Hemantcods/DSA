"""

B. Beautiful Array


number of elements, k ,beauty value, sum of elements


        n k b s    
input : 5 4 7 38
output: 0 3 3 3 29
"""

def solve(n,k,b,s):
    arr=[0]*n
    mnSum=b*k
    mxSum=b*k+(n*(k-1))
    if s<mnSum:
        return -1
    if s>mxSum:
        return -1
    arr[n-1]=mnSum
    extra=s-mnSum
    take=min(extra,k-1)
    arr[n-1]+=take
    extra-=take
    for i in range(n-2,-1,-1):
        give=min(extra,k-1)
        arr[i]+=give
        extra-=give
    return arr