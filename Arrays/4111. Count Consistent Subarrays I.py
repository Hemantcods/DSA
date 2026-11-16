class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            val=nums[i]
            minV=nums[i]
            for j in range(i,n):
                val=val&nums[j]
                minV=min(minV,nums[j])
                if val==minV:
                    ans+=1
        return ans
