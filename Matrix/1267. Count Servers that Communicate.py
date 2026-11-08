class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n,m=len(grid),len(grid[0])
        total=0
        colServerCount=[0]*m
        rowServerCount=[0]*n
        disConnected=0
        for r in range(n):
            for c in  range(m):
                if grid[r][c]==1:
                    total+=1
                    colServerCount[c]+=1
                    rowServerCount[r]+=1
        for r in range(n):
            for c in  range(m):
                if grid[r][c]==1:
                    # check if it is disconneced
                    if rowServerCount[r]==1 and colServerCount[c]==1:
                        disConnected+=1
        return total-disConnected
# Time Complexity - O(mn+mn) -> O(mn)
# Space Complexity - O(m+n)