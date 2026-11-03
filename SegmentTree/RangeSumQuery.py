# code for querying from the segment tree
# Ex-range sum querry
# 
segTree=[]
def Querry( start,end,idx,l,r):
    if (l>end or r<start):
        return 0
    if (l>=start and r<=end):
        return segTree[idx]
    mid=l+(r-l)//2
    return Querry(start,end,2*idx+1,l,mid)+Querry(start,end,2*idx+2,mid+1,r)

# Heignt of segment Tree is log(n)
# Time complexity--->2*log(n)-> log(n)
