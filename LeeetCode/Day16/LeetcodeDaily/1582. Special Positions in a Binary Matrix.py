class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        rcount=[0]*m
        ccount=[0]*n
        count=0
        for r in range(m):
            for c in range(n):
                if mat[r][c]==1:
                    rcount[r]+=1
                    ccount[c]+=1
        for r in range(m):
            for c in range(n):
                if mat[r][c]==1:
                    if rcount[r]==1 and ccount[c]==1:
                        count+=1
        return count                

                   




                
                        