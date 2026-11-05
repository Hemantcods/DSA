class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        dp=[None]*n        
        def solve(idx):
            if idx>=n-1:
                return True
            if dp[idx]!=None:
                return dp[idx]
            mxJump=nums[idx]
            for i in range(mxJump,0,-1):
                if solve(idx+i):
                    dp[idx]=True
                    return dp[idx]
            dp[idx]=False
            return False
        return solve(0)


# Optimized car petrol Aproach
# assuming the max petrol for each step is max(petrol,nums[i]) then reducing petrol by 1 for each step
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        petrol = 0
        for p in nums :
            if petrol < 0 : return False
            if p > petrol :
                petrol=p
            petrol -= 1
        return True