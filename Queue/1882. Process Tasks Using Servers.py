# Submission 1st - Error in time management when no free Server 
import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        freeServers=[]
        # adding servers to free server heap 
        for idx in range(len(servers)):
            heapq.heappush(freeServers,(servers[idx],idx))
        occupiedServers=[]
        time=0
        ans=[]
        for t in tasks:
            # free the occupied server and add them to free
            print(freeServers,occupiedServers)
            while len(occupiedServers)>0:
                ft,s,idx=occupiedServers[0]
                if ft>time:
                    break
                heapq.heappop(occupiedServers)
                # adding to free server list
                heapq.heappush(freeServers,(s,idx))
            # check if there is free servers
            if len(freeServers)==0:
                ans.append(0)
                time+=1
                continue
            # pull out the free server
            s,idx=heapq.heappop(freeServers)
            ans.append(idx)
            # add the server to occupied server
            heapq.heappush(occupiedServers,(time+t,s,idx))
            time+=1
        return ans

# Corrected Submission
# Direct skipping time to the next nearest server
import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        freeServers=[]
        # adding servers to free server heap 
        for idx in range(len(servers)):
            heapq.heappush(freeServers,(servers[idx],idx))
        occupiedServers=[]
        time=0
        ans=[]
        for i,t in enumerate(tasks):
            time=max(time,i)
            # free the occupied server and add them to free
            while len(occupiedServers)>0:
                ft,s,idx=occupiedServers[0]
                if ft>time:
                    break
                heapq.heappop(occupiedServers)
                # adding to free server list
                heapq.heappush(freeServers,(s,idx))
            # check if there is free servers
            if len(freeServers)==0:
                # check the nearest free server 
                time = occupiedServers[0][0]
                # Release all servers available at this time
                while occupiedServers and occupiedServers[0][0] <= time:
                    ft, s, idx = heapq.heappop(occupiedServers)
                    heapq.heappush(freeServers, (s, idx))
            # pull out the free server
            s,idx=heapq.heappop(freeServers)
            ans.append(idx)
            # add the server to occupied server
            heapq.heappush(occupiedServers,(time+t,s,idx))
        return ans