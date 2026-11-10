class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        m=len(a)
        n=len(b)
        mFull=m*x
        nFull=n*y
        if mFull<nFull:
            return False
        LCM=lcm(m,n)
        for i in range(m):
            matched=True
            for j in range(min(LCM,nFull)):
                if b[j%n]!=a[(i+j)%m]:
                    matched=False
                    break
            if matched and (i+nFull<=mFull):
                return True
        return False