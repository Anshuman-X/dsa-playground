class Graph:
    def __init__(self):
        self.adjList = {}
        
    def add_vertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
            
    def addEdge(self,src,dest):
        self.add_vertex(src)
        
        self.adjList[src].append(dest)
        
    def printGraph(self):
        for vertex in self.adjList:
            print(vertex,"->",self.adjList[vertex])
            
g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,2)
g.addEdge(3,4)
g.addEdge(2,4)
g.printGraph()