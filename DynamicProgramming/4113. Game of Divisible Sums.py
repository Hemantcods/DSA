# Normal DP
class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[[-1]*2 for _ in range(n)]
        # Alice Starts
        # sate index,player
        # A->0 and B->1
        def solve(i,player):
            if i==n:
                return 0
            if dp[i][player]!=-1:
                return dp[i][player]
            take2=float('-inf')
            take1=nums[i]
            if take1%3==0:
                take1+=solve(i+1,1)
            else:
                take1+=solve(i+1,0)
            if i<n-1:
                take2=nums[i]+nums[i+1]
                if take2%3==0:
                    take2+=solve(i+2,1)
                else:
                    take2+=solve(i+2,0)
            if player==0:
                dp[i][player]=max(take1,take2)
                return dp[i][player]
            else:
                dp[i][player]=-1*max(take1,take2)
                return dp[i][player]
        return solve(0,0)

# Bottom Up
class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[0]*(n+1)
        # Base condition
        for i in range(n-1,-1,-1):
            take1=nums[i]
            if take1%3==0:
                take1-=dp[i+1]
            else:
                take1+=dp[i+1]
            if i+1<n:
                take2=nums[i+1]+nums[i]
                if take2%3==0:
                    take2-=dp[i+2]
                else:
                    take2+=dp[i+2]
                dp[i]=max(take1,take2)
            else:
                dp[i]=take1
        return dp[0]

# Most Optimal with O(1) space
class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n=len(nums)
        dp1,dp2=nums[-1],0
        # Base condition
        for i in range(n-2,-1,-1):
            take1=nums[i]-dp1 if nums[i]%3==0 else nums[i]+dp1
            take2=nums[i]+nums[i+1]-dp2 if (nums[i]+nums[i+1])%3==0 else nums[i]+nums[i+1]+dp2
            dp2,dp1=dp1,max(take1,take2)         
        return dp1