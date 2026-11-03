class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        MOD=12345
        suffix=1
        p=[[0 for _ in range(n)]for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                p[i][j]=suffix
                suffix=(suffix*grid[i][j])%MOD
        prefix=1
        for i in range(m):
            for j in range(n):
                p[i][j]=(prefix*p[i][j])%MOD
                prefix=(prefix*grid[i][j])%MOD        
        return p