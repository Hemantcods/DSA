class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        index={}
        for k in range(n):
            if nums[k] not in index:
                index[nums[k]] = []
            index[nums[k]].append(k)
            if len(index[nums[k]])>=3:
                siz=len(index[nums[k]])
                i=index[nums[k]][siz-3]
                if res!=0:
                    res=min(res,2*(k-i))
                else:
                    res=2*(k-i)   
        if (res!=0): return res
        else: return -1                    