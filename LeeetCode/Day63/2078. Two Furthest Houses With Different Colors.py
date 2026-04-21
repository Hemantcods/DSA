class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        res=0
        for i in range(n):
            if colors[0]!=colors[i]:
                res=max(res,i)
            if colors[n-1]!=colors[i]:
                res = max(res, n - 1 - i)  
        return res        
    