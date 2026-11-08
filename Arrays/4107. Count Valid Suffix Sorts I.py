from collections import Counter
class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        # valid if nums[:i]==target[:i]
        # check target[i:] is decreasing
        n=len(nums)
        if Counter(nums) != Counter(target):
            return 0
        isDecreasing=[True]*n
        for i in range(n-2,-1,-1):
            isDecreasing[i]=isDecreasing[i+1] and target[i]>=target[i+1]
        prefixMatch=True
        ans=0
        for i in range(n):
            if prefixMatch and isDecreasing[i]:
                ans+=1
            if  nums[i]!=target[i]:
                prefixMatch=False
        return ans