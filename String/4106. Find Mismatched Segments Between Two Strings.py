class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        misMatchs1=""
        misMatchs2=""
        n=len(s1)
        ans =[]
        for i in range(n):
            if s1[i]==s2[i]:
                if len(misMatchs1)>0:
                    ans.append([misMatchs1,misMatchs2])
                    misMatchs1,misMatchs2="",""
            else:
                misMatchs1+=s1[i]
                misMatchs2+=s2[i]
        if len(misMatchs1)>0:
            ans.append([misMatchs1,misMatchs2])
        return ans
        