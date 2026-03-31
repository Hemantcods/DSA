class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        result=[[0 for _ in range(n-k+1)]for _ in range(m-k+1)]

        for r in range(m-k+1):
            for c in range(n-k+1):
                val=[]
                for r_ in range(r,r+k):
                    for c_ in range(c,c+k):
                        val.append(grid[r_][c_])
                prev=None
                minimum= float('inf')
                val.sort()
                for value in val:
                    if prev is not None:
                        if value!=prev:
                            diff=abs(prev-value)
                            minimum=min(diff,minimum)
                    prev=value
                if minimum == float('inf'):
                    minimum=0  
                result[r][c]=minimum 
        return result       
