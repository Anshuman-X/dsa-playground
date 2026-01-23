class deque:
    def __init__(self):
        self.items = []
        self.front = 0
        
    def isEmpty(self):
        return self.front >= len(self.items)
    def insertRear(self,value):
        return self.items.append(value)
    def deleteFront(self):
        if self.isEmpty():
            return None
        else:
            value = self.items[self.front]
            self.front += 1
            return value
        
class Graph:
    def __init__(self,vertex):
        self.mat = [[0]*vertex for _ in range(vertex)]
        self.size = vertex
        
    def addEdge(self,src,dest):
        if 0<=src<self.size and 0<=dest<self.size:
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Inavlid Edge")
    
    def BFS(self,src):
        visited = [False]*self.size
        dq = deque()
        dq.insertRear(src)
        visited[src] = True

        print("BFS Traversal: ")
        while not dq.isEmpty():
            v = dq.deleteFront()
            print(v,end=" ")
            
            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    visited[i] = True
                    dq.insertRear(i)
                    
g = Graph(8)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,3)
g.addEdge(3,5)
g.addEdge(3,4)
g.addEdge(5,4)
g.addEdge(4,6)
g.addEdge(6,2)
g.addEdge(6,7)

g.BFS(0)