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
    def dfs(self,src):
        visited=[False]*self.size
        stack=[src]
        while(stack):
            v=stack.pop()
            if visited[v]==False:
                print(v,end="->")
                visited[v]=True
            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    stack.append(i)
        print("\n")                    
                    
g=Graph(6)
g.add_edge(0,1)              
g.add_edge(0,2)              
g.add_edge(2,3)              
g.add_edge(2,4)              
g.add_edge(3,5)              
g.add_edge(4,5)              
g.print()
g.dfs(0)



