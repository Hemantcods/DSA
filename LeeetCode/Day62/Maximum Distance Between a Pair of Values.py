class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res=0
        n=len(nums1)
        m=len(nums2)
        i,j=0,0
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                res=max(res,j-i)
                j+=1
            else:
                i+=1
        return res            