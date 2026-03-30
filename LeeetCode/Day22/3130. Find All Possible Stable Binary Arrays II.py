class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]
        
        for i in range(0, min(zero, limit)+1):
            dp0[i][0] = 1
        for j in range(0, min(one, limit)+1):
            dp1[0][j] = 1
        
        for i in range(zero+1):
            for j in range(one+1):
                if (i==0 or j==0):
                    continue
                dp1[i][j]=(dp0[i][j-1]+dp1[i][j-1])%MOD
                if(j-1>=limit):
                    dp1[i][j]=(dp1[i][j]-dp0[i][j-1-limit]+MOD)%MOD
                dp0[i][j]=(dp0[i-1][j]+dp1[i-1][j])%MOD
                if(i-1>=limit):
                    dp0[i][j]=(dp0[i][j]-dp1[i-1-limit][j]+MOD)%MOD    
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD