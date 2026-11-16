class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        n=len(parent)
        children=[[]for _ in range(n)]
        for i in range(1,n):
            children[parent[i]].append(i)
        dp=[0]*n
        order=[0]
        for u in order:
            for v in children[u]:
                order.append(v)
        for u in reversed(order):
            # if it is a leaf node 
            # do nothing
            if not children[u]:
                dp[u]=score[u]
                continue
            total=0
            minChildNode=float('inf')
            for v in children[u]:
                total+=dp[v]
                minChildNode=min(minChildNode,dp[v])

            if op[u]==0:
                dp[u]=score[u]+total-min(minChildNode,0)
            else:
                dp[u]=score[u]+total-minChildNode
        return dp[0]
            
        
        