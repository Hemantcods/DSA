class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        flip1,flip2=0,0
        res = float("inf")
        l=0
        for r in range(2*n):
            expected_s1="0" if r%2==0 else '1'
            expected_s2="1" if r%2==0 else '0'
            if s[r%n] != expected_s1:
                flip1 += 1
            if s[r%n] != expected_s2:
                flip2 += 1
            
            if r - l + 1 > n:
                expected_s1="0" if l%2==0 else '1'
                expected_s2="1" if l%2==0 else '0'
                if s[l%n] != expected_s1:
                    flip1 -= 1
                if s[l%n] != expected_s2:
                    flip2 -= 1
                l += 1
            if r - l + 1 == n:
                res = min(res, flip1, flip2)
        return res        

