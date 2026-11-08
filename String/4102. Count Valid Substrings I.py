class Solution:
    def countValidSubstrings(self, s: str) -> int:
        ans=0
        last=-1
        n=len(s)
        total=(n*(n+1))//2
        for j in range(n):
            if j>=2 and s[j-2:j+1]=='abc':
                last=j-2
            if last!=-1:
                ans+=last+1
        return total-ans
        