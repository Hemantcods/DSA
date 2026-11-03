class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def checkHors(total,grid):
            r,c=len(grid),len(grid[0])
            seen=set()
            top=0
            for i in range(r-1):
                for j in range(c):
                    seen.add(grid[i][j])
                    top+=grid[i][j]
                bottom=total-top    
                diff=top-bottom 
                if (diff==0  or  diff==grid[0][0] or diff==grid[0][c-1] or diff==grid[i][0]):
                    return True
                if (i>0 and c>1 and diff in seen):
                    return True
            return False    

        r,c=len(grid),len(grid[0])
        total=0
        for i in range(r):
            for j in range(c):
                total+=grid[i][j]

        if(checkHors(total,grid)):
            return True
        grid = list(zip(*grid[::-1]))
        if(checkHors(total,grid)):
            return True
        grid = list(zip(*grid[::-1]))
        if(checkHors(total,grid)):
            return True
        grid = list(zip(*grid[::-1]))  
        if(checkHors(total,grid)):
            return True    
        return False