class Graph:
    def __init__(self):
        self.adjList = {}
        
    def add_vertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
            
    def addEdge(self,src,dest,weight):
        self.add_vertex(src)
        # self.add_vertex(dest)
        
        if (weight,dest) not in self.adjList[src]:
            self.adjList[src].append((weight,dest))
            
        # if (weight,src) not in self.adjList[dest]:
        #     self.adjList[dest].append((weight,src))
            
    def printGraph(self):
        for vertex in self.adjList:
            print(vertex,"->",self.adjList[vertex])
            
g = Graph() 
g.addEdge(1,2,6)
g.addEdge(1,3,9)
g.addEdge(3,2,10)
g.addEdge(3,4,3)
g.addEdge(2,4,5)

g.printGraph()