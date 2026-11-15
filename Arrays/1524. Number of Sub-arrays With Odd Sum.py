# Submission : 1
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD=10**9 +7
        s=0
        even=1
        ans=0
        odd=0
        n=len(arr)
        for i in range(n):
            s+=arr[i]
            # IF EVEN+ODD=ODD 
            if s%2!=0:
                ans=(ans+even)%MOD
                odd+=1
            # IF ODD+EVEN=ODD
            else:
                ans=(ans+odd)%MOD
                even+=1
        return ans   
