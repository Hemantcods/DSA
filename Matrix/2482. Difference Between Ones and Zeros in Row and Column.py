class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        r_ones=[0]*m
        c_ones=[0]*n
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    r_ones[r]+=1
                    c_ones[c]+=1
        for r in range(m):
            for c in range(n):
                grid[r][c]=2*(r_ones[r]+c_ones[c])-m-n
        return grid        