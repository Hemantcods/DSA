# Brute force aproach
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for qur in queries:
            idx=qur[0]
            while(idx<=qur[1]):
                nums[idx]=(nums[idx]*qur[3])%(10**9+7)
                idx+=qur[2]
        res=0    
        for num in nums:
            res=res^num
        return res    
