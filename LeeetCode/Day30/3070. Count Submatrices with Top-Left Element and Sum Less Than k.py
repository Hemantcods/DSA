class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0]>k:
            return 0
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i-1>=0):grid[i][j]+=grid[i-1][j]
                if(j-1>=0):grid[i][j]+=grid[i][j-1]
                if(i-1>=0 and j-1>=0):grid[i][j]-=grid[i-1][j-1]

                if (grid[i][j]<=k):
                    count+=1
                else:
                    break
        return count                