# Submission 1:
# TLE

import heapq
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        ServerRequests=[[0,i]for i in range(k)]
        # (No of requests,serveridx)
        occupiedServer=[]
        # (freeTime,serveridx)
        isFree=[True]*k
        assignedServer=0
        n=len(load)
        t=1
        for i in range(n):
            cost=load[i]
            time=arrival[i]
            t=max(time,t)
            # free the occupied servers
            while len(occupiedServer)>0:
                ft,s=occupiedServer[0]
                if ft>t:
                    break
                heapq.heappop(occupiedServer)
                isFree[s]=True
                assignedServer-=1
            # Assign Requests
            # check for free servers
            if assignedServer==k:
                continue
            for j in range(k):
                index=(i+j)%k
                if not isFree[index]:
                    continue
                heapq.heappush(occupiedServer,(t+cost,index))
                ServerRequests[index][0]+=1
                isFree[index]=False
                assignedServer+=1
                break
        ServerRequests.sort()
        prev=ServerRequests[-1][0]
        ans=[]
        for i in range(k):
            req,idx=ServerRequests[k-i-1]
            if prev>req:
                break
            ans.append(idx)
            prev=req
        return ans


# Submission: 2
# optimised usind Sorted Array and BS

import heapq
from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        ServerRequests=[[0,i]for i in range(k)]
        # (No of requests,serveridx)
        occupiedServer=[]
        # (freeTime,serveridx)
        freeServers=SortedList(range(k))
        n=len(load)
        t=1
        for i in range(n):
            cost=load[i]
            time=arrival[i]
            t=max(time,t)
            # free the occupied servers
            while len(occupiedServer)>0:
                ft,s=occupiedServer[0]
                if ft>t:
                    break
                heapq.heappop(occupiedServer)
                freeServers.add(s)
            # Assign Requests
            # check for free servers
            if len(freeServers)==0:
                continue
            index=freeServers.bisect_left(i%k)
            if index==len(freeServers):
                index=0
            s=freeServers.pop(index)
            heapq.heappush(occupiedServer,(t+cost,s))
            ServerRequests[s][0]+=1
        ServerRequests.sort()
        prev=ServerRequests[-1][0]
        ans=[]
        for i in range(k):
            req,idx=ServerRequests[k-i-1]
            if prev>req:
                break
            ans.append(idx)
            prev=req
        return ans