# Submission:1
# Normal DP approach+memonisation

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp=[-1]*n
        def solve(i):
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            oneJ=float('inf')
            twoJ=float('inf')
            threeJ=float('inf')
            if i+1<=n:
                oneJ=1+solve(i+1)+costs[i]
            if i+2<=n:
                twoJ=4+solve(i+2)+costs[i+1]
            if i+3<=n:
                threeJ=9+solve(i+3)+costs[i+2]
            dp[i]=min(oneJ,twoJ,threeJ)
            return dp[i]
        return solve(0)

# Time Complexity O(n)
# Space Complexity O(n)

# Optimized DP 
class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        costs = [0] + costs
        a, b, c = costs[n], inf, inf  # dp[i + 1], dp[i + 2], dp[i + 3] for i = n - 1
        for i in reversed(range(n)):
            a, b, c = costs[i] + min(a + 1, b + 4, c + 9), a, b
        return a
# Time Complexity O(n)
# Space Complexity O(1)