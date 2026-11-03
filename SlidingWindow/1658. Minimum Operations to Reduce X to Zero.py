class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target=sum(nums)-x
        if target<0:
            return -1
        cur=0
        left=0
        max_len=-1
        for right in range(n):
            cur+=nums[right]
            while cur>target:
                cur-=nums[left]
                left+=1
            if cur==target:
                max_len=max(max_len,right-left+1)
        if max_len==-1:
            return -1
        return n-max_len


sol = Solution()

nums = [3,2,20,1,1,3]
x = 10

print(sol.minOperations(nums, x))