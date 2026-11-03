class Solution:
    def minimumDistance(self, word: str) -> int:
        self.dp=[[[-1 for _ in range(27)]for _ in range(27)]for _ in range(301)]
        return self.solve(0,26,26,word)
    def dist(self,a,b):
        if (a==26 or b==26): return 0
        r1,c1=a//6,a%6
        r2,c2=b//6,b%6
        return abs(r1-r2)+abs(c1-c2)
    def solve(self,i,f1,f2,word):
        if i==len(word): return 0
        if (self.dp[i][f1][f2]!=-1):
            return self.dp[i][f1][f2]
        curr = ord(word[i]) - ord('A')
        move1=self.dist(f1,curr)+self.solve(i+1,curr,f2,word)
        move2=self.dist(f2,curr)+self.solve(i+1,f1,curr,word)
        self.dp[i][f1][f2]=min(move1,move2)
        return self.dp[i][f1][f2]


