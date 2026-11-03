from collections import deque
class Graph:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for _ in range(vertex) ]
        self.size=vertex
    def add_edge(self,source,destination):
        if (0<=source<self.size and 0<=destination<self.size):
            self.mat[source][destination]=1
            # for undirected
            self.mat[destination][source]=1
        else:
            print("Invalid edge")
    def print(self):
        for row in self.mat:
            print(' '.join(map(str,row)))

    def BFS(self,src):
        visited=[False]*self.size
        queue=deque([src])
        visited[src]=True
        while queue:
            v=queue.popleft()
            print(v,end=" ")
            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    visited[i]=True 
                    queue.append(i)

g=Graph(8)
g.add_edge(0,1)              
g.add_edge(0,3)              
g.add_edge(1,3)              
g.add_edge(3,5)              
g.add_edge(3,4)              
g.add_edge(4,5)              
g.add_edge(4,6)              
g.add_edge(6,2)              
g.add_edge(6,7)              

g.BFS(0)



