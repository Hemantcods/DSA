class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        list=[]
        start=0
        sum=0
        for i in range(len(s)):
            if s[i]=="1":
                sum+=1
            else:
                sum-=1
            if sum==0:
                list.append("1"+self.makeLargestSpecial(s[start+1:i])+"0")
                start=i+1
        list.sort(reverse=True)
        return "".join(list)
    
            