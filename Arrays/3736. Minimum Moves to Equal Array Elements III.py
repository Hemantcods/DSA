# just count the diffeence from the max element 
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        high=max(nums)
        ans=0
        for num in nums:
            ans+=(high-num)
        return ans
# Time Complexity: O(n)
# Space Complexity: O(1)