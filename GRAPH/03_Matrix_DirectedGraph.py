class Graph:
    def __init__(self,vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self,src,dest):
        if(0 <= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest] = 1
            
        else:
            print("Invalid Edge")
            
    def display(self):
        for row in self.mat:
            print(' '.join(map(str,row)))
            
G = Graph(5)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,3)

G.display()