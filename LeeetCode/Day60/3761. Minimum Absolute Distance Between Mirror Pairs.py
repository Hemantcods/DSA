class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n=len(nums)
        res=float('inf')
        last_seen={}
        for i, num in enumerate(nums):
            rev = self.reverse(num)
            if num in last_seen:
                res = min(res, abs(i - last_seen[num]))
            last_seen[rev] = i
        if res==float('inf'):
            return -1                   
        return res
    def reverse(self,num):
        while(num%10==0):
            num=int(num/10)     
        return int(str(num)[::-1])