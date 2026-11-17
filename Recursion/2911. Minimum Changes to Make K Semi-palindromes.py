# Submission 1 with MEMONISATION
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n=len(s)
        memCost=[[-1]*n for _ in range(n)]
        memSolve=[[-1]*(k+1) for _ in range(n+1)]
        def getCost(st,ed):
            size=ed-st+1
            minCost=float('inf')
            if memCost[st][ed]!=-1:
                return memCost[st][ed]
            for d in range(1,size):
                if size%d!=0:
                    continue
                # Making groups
                cost=0
                for group in range(d):
                    l=st+group
                    r=l+(size//d -1)*d
                    while (l<r):
                        if s[l]!=s[r]:
                            cost+=1
                        l+=d
                        r-=d
                minCost=min(minCost,cost)
            memCost[st][ed]=minCost
            return minCost
        def solve(start,k):
            if k==0:
                if start==n:
                    return 0
                else:
                    return float('inf')
            minCst=float('inf')
            if start+2*k>n:
                return float('inf')
            if memSolve[start][k]!=-1:
                return memSolve[start][k]
            for end in range(start+1,n-2*(k-1)):
                minCst=min(getCost(start,end)+solve(end+1,k-1),minCst)
            memSolve[start][k]=minCst
            return minCst
        return solve(0,k)


# Submission 2 with Bottom up
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n=len(s)
        memCost=[[-1]*(n+1) for _ in range(n+1)]
        memSolve=[[float('inf')]*(k+1) for _ in range(n+1)]
        def getCost(st,ed):
            size=ed-st+1
            minCost=float('inf')
            if memCost[st][ed]!=-1:
                return memCost[st][ed]
            for d in range(1,size):
                if size%d!=0:
                    continue
                # Making groups
                cost=0
                for group in range(d):
                    l=st+group
                    r=l+(size//d -1)*d
                    while (l<r):
                        if s[l]!=s[r]:
                            cost+=1
                        l+=d
                        r-=d
                minCost=min(minCost,cost)
            memCost[st][ed]=minCost
            return minCost
        # filling the memCost first
        for i in range(n):
            for j in range(i+1,n):
                memCost[i][j]=getCost(i,j)

        # memSolve Base Case
        memSolve[n][0]=0
        for start in range(n-1,-1,-1):
            for peices in range(1,k+1):
                if start+2*peices>n:
                    continue
                res=float('inf')
                for end in range(start+1,n):
                    res=min(res,memSolve[end+1][peices-1]+memCost[start][end])
                memSolve[start][peices]=res
        return memSolve[0][k]