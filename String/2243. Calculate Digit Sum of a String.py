class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            sum=0
            newS=''
            for i in range(len(s)):
                sum+=(int(s[i]))
                if (i+1)%k==0:
                    newS+=str(sum)
                    sum=0
            if len(s)%k!=0:
                newS+=str(sum)
            s=newS
        return s