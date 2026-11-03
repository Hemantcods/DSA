class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res=0
        n=len(nums)
        i,j=start,start
        while True:
            if nums[i]==target or nums[j]==target:
                break
            else:
                res+=1
                if i>0:
                    i-=1
                if j<n-1:
                    j+=1

        return res            
             
        