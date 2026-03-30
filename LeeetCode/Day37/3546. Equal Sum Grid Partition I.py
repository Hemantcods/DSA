class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        r,c=len(grid),len(grid[0])
        total=0
        rowsum=[0 for _ in range(r)]
        colsum=[0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                total+=grid[i][j]
                rowsum[i]+=grid[i][j]
                colsum[j]+=grid[i][j]
        if total%2!=0:
            return False
        # horizontal split
        upper=0
        for i in range(r-1):
            upper+=rowsum[i]
            if upper==total-upper:
                return True
        #veritcal split
        left=0
        for i in range(c-1):
            left+=colsum[i]
            if left==total-left:
                return True
        return False