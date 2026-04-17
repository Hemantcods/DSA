class Graph:
    def __init__(self):
        self.adjList={}
    def add_vertex(self,vertex):  
        if vertex not in self.adjList:
            self.adjList[vertex]=[]
    def addEdge(self,src,des):
        self.add_vertex(src)            
        self.add_vertex(des)
        self.adjList[src].append(des)            
        self.adjList[des].append(src)            
    def PrintGraph(self):
        for vertex in self.adjList:
            print(vertex,"->",self.adjList[vertex],end='\n')

g=Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(4,3)                    
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,5)


g.PrintGraph()