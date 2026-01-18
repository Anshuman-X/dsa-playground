class Graph:
    def __init__(self,vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self,src,dest,weight):
        if(0 <= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest] = weight
            self.mat[dest][src] = weight
            
        else:
            print("Invalid Edge")
            
    def display(self):
        for row in self.mat:
            print(' '.join(map(str,row)))
            

G=Graph(6)

G.add_edge(1,2,5)
G.add_edge(1,3,2)  
G.add_edge(3,4,6)
G.add_edge(2,5,8)
G.add_edge(4,5,9)

G.display()