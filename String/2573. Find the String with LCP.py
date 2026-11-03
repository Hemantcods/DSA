class Solution:
    def checkLCP(self,string,lcp):
        n=len(lcp)
        nlcp = [[0]*n for _ in range(n)]
        for i in range(n):
            nlcp[i][n-1]=1 if string[i]==string[n-1] else 0
        for i in range(n):
            nlcp[n-1][i]=1 if string[n-1]==string[i] else 0    
        for i in range(n-2,-1,-1):
            for j in range(n-2,-1,-1):
                if string[i]==string[j]:
                    nlcp[i][j]=1+nlcp[i+1][j+1]
                else:
                    nlcp[i][j]=0             
        return nlcp==lcp
    def findTheString(self, lcp: List[List[int]]) -> str:
        n=len(lcp)
        word = ["$"] * n
        if lcp[0][0]==0:
            return ''
        word[0]='a'
        for i in range(n):
            for j in range(i):
                if lcp[i][j]!=0:
                    word[i]=word[j]
                    break
            if word[i]=="$":
                forbidden=[False for _ in range(26)]  
                for j in range(i):
                    if lcp[i][j]==0:
                        forbidden[ord(word[j])-ord('a')]=True 
                for idx in range(26):
                    if forbidden[idx]==False:
                        word[i]=chr(idx+ord('a'))
                        break
                if word[i]=='$':
                    return ''  

        return ''.join(word) if self.checkLCP(''.join(word),lcp) else ""                          
                        

