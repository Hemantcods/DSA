from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        idx_ct= defaultdict(int)
        idx_sum=defaultdict(int)
        for i in range(n):
            sum=(idx_ct[nums[i]]*i)-idx_sum[nums[i]]
            res.append(sum)
            idx_ct[nums[i]]+=1
            idx_sum[nums[i]]+=i
        idx_ct= defaultdict(int)
        idx_sum=defaultdict(int)
        for i in range(n-1,-1,-1):
            sum=idx_sum[nums[i]]-(idx_ct[nums[i]]*i)
            res[i]+=sum
            idx_ct[nums[i]]+=1
            idx_sum[nums[i]]+=i
        return res