# Submission 1
# TLE - Unoptimal
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        req=[[]for _ in range(n)]
        logs.sort(key=lambda x:x[1])
        ans=[0]*len(queries)
        for s,t in logs:
            req[s-1].append(t)
        for i in range(len(queries)):
            q=queries[i]
            lower=q-x
            for s in range(n):
                idx=bisect_right(req[s],q)-1
                if idx==-1:
                    ans[i]+=1
                    continue
                last=req[s][idx]
                if last<lower or last>q:
                    ans[i]+=1
        return ans

# Submission 2 TLE
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        def binarySearch(arr,target):
            l,r=0,len(arr)
            while l<r:
                mid=l+(r-l)//2
                if arr[mid][1]<target:
                    l=mid+1
                else:
                    r=mid
            return l
        # optimal
        logs.sort(key=lambda x:x[1])
        ans=[0]*len(queries)
        for i in range(len(queries)):
            upper=queries[i]
            lower=upper-x
            # Binary search to find the nearest index
            idx=binarySearch(logs,lower)
            # start the loop to find the non active servers
            s=set()
            for j in range(idx,len(logs)):
                server,time=logs[j]
                if time>upper:
                    break
                s.add(server)
            ans[i]=n-len(s)
        return ans

# Final Submission 3 using Sliding Window
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # most optimal using sliding window
        logs.sort(key=lambda x:x[1])
        # sorting querry for applying Sliding Window
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        ans=[0]*len(queries)
        count=[0]*n
        active=0
        i,j=0,0
        m=len(logs)
        for q,idx in sorted_queries:
            lower=q-x
            # set position of j pointer
            while j<m and logs[j][1]<=q:
                server,time=logs[j]
                if count[server-1]==0:
                    active+=1
                count[server-1]+=1
                j+=1
            # set position of i pointer
            while i<j and logs[i][1]<lower:
                server,time=logs[i]
                count[server-1]-=1
                if count[server-1]==0:
                    active-=1
                i+=1
            ans[idx]=n-active
        return ans
# Time Complexity O(mlogm+l log l)