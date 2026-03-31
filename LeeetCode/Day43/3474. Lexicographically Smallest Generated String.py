class Solution:
    def isSame(self,word,str2,i,m):
        for j in range(m):
            if word[i]!=str2[j]:
                return False
            i+=1
        return True      

    def generateString(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        N=n+m-1
        word=[' ']*N
        canChange=[False]*N
        for i in range(n):
            if str1[i]=="T":
                _i=i
                for j in range(m):
                    if (word[_i]!=" " and word[_i]!=str2[j]):
                        return ''
                    word[_i]=str2[j]
                    _i+=1
        # filling the remainig spaces
        for i in range(N):
            if word[i]==' ':
                word[i]="a"
                canChange[i]=True             
        # process F 
        for i in range(n):
            if str1[i]=="F":
                if (self.isSame(word,str2,i,m)):
                    changed=False
                    for k in range(i+m-1,i-1,-1):
                        if canChange[k]:
                            word[k]='b'
                            changed=True
                            break
                    if changed==False:
                        return ""
        return "".join(word)                             