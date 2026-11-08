# NOT SOLVED MYSELF (used ai)
class Solution:
    def countValidSubstrings(self, s: str) -> int:
        # index,last
        last_a=-1
        last_ab=-1
        last_invalid=-1
        ans=0
        n=len(s)
        for j in range(n):
            if s[j]=='a':
                last_a=j
            if s[j]=='b':
                if last_a!=-1:
                    last_ab=last_a
            if s[j]=='c':
                if last_ab!=-1:
                    last_invalid=last_ab
            if last_invalid!=-1:
                ans+=j-last_invalid
            else:
                ans+=j+1
        return ans