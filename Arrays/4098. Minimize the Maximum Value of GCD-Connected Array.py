# Brute Force Approcah gives TLE

class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        cnt=0
        prev=value
        for i in range(value-1,1,-1):
            if gcd(prev,i)>1:
                prev=i
                cnt+=1
        if cnt<index:
            return -1
        
        cur=value+1
        prev=value
        cnt=0
        while True:
            if gcd(cur,prev)>1:
                prev=cur
                cnt+=1
            if cnt==n-index-1:
                return cur
            cur+=1
# Brute Force Complexity:
# Time Complexity: O(value * log(value) + n * log(value + n))
# Space Complexity: O(log(value + n))  (recursion stack for gcd)

# Optimized approcach 

class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        # use smallest prime Factor
        # next and prev always even
        # then use always 2
        if value==1:
            return -1
        def minPrimeF(num):
            i=2
            while i*i<=value:
                if num%i==0:
                    return i
                i+=1
            return num
        p=minPrimeF(value)
        leftCnt=(value-p)//2
        if leftCnt<index:
            return -1
        x=n-index-2
        if x<0:
            return value
        return value+p+(2)*(x)

# Optimized Complexity:
# Time Complexity: O(sqrt(value))
# Space Complexity: O(1)