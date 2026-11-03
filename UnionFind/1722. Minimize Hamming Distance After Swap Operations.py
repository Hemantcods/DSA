from collections import defaultdict,Counter
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n=len(source)
        rank=[0]*n
        parent=[-1]*n
        def Find(x):
            if parent[x]!=x:
                parent[x]=Find(parent[x])
            return parent[x] 
        def Union(x,y):
            rootX=Find(x)
            rootY=Find(y)
            if rootX==rootY: return
            if rank[rootX]<rank[rootY]:
                rootX,rootY=rootY,rootX
            parent[rootY]=rootX
            if rank[rootX]==rank[rootY]:
                rank[rootX]+=1
            
        for i in range(n):
            parent[i]=i
        # Union of allowed swaps
        for elem in allowedSwaps:
            Union(elem[0],elem[1])
        # unordered map for storing frequency and indexes
        mp = defaultdict(Counter)  
        for i in range(n):
            root = Find(i)
            mp[root][source[i]] += 1
        res = 0
        for i in range(n):
            root = Find(i)
            if mp[root][target[i]] > 0:
                mp[root][target[i]] -= 1
            else:
                res += 1
        return res