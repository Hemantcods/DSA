class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        
        # dp[j][k] = max money at column j with k skips left
        dp = [[-10**15] * 3 for _ in range(n)]
        
        # Initialize bottom-right
        for k in range(3):
            if coins[m-1][n-1] < 0 and k > 0:
                dp[n-1][k] = 0
            else:
                dp[n-1][k] = coins[m-1][n-1]
        
        # Fill last row
        for j in range(n-2, -1, -1):
            for k in range(3):
                val = coins[m-1][j]
                
                take = val + dp[j+1][k]
                skip = dp[j+1][k-1] if val < 0 and k > 0 else -10**15
                
                dp[j][k] = max(take, skip)
        
        # Process rows bottom-up
        for i in range(m-2, -1, -1):
            new_dp = [[-10**15]*3 for _ in range(n)]
            
            # last column
            for k in range(3):
                val = coins[i][n-1]
                
                take = val + dp[n-1][k]
                skip = dp[n-1][k-1] if val < 0 and k > 0 else -10**15
                
                new_dp[n-1][k] = max(take, skip)
            
            # rest of row
            for j in range(n-2, -1, -1):
                for k in range(3):
                    val = coins[i][j]
                    
                    best_next = max(dp[j][k], new_dp[j+1][k])
                    
                    take = val + best_next
                    skip = max(
                        dp[j][k-1],
                        new_dp[j+1][k-1]
                    ) if val < 0 and k > 0 else -10**15
                    
                    new_dp[j][k] = max(take, skip)
            
            dp = new_dp
        
        return max(dp[0])