class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        count=0
        r=len(grid)
        c=len(grid[0])
        gridx=[[0 for _ in range(c) ]for _ in range(r)]
        gridy=[[0 for _ in range(c) ]for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="X":
                    gridx[i][j]=1
                elif grid[i][j]=="Y":
                    gridy[i][j]=1

                if(i-1>=0):
                    gridx[i][j]+=gridx[i-1][j]
                    gridy[i][j]+=gridy[i-1][j]

                if(j-1>=0):
                    gridx[i][j]+=gridx[i][j-1]
                    gridy[i][j]+=gridy[i][j-1]

                if(i-1>=0 and j-1>=0):
                    gridx[i][j]-=gridx[i-1][j-1]
                    gridy[i][j]-=gridy[i-1][j-1]

                if (gridx[i][j]>0 and gridx[i][j]==gridy[i][j]):
                    count+=1
        return count            