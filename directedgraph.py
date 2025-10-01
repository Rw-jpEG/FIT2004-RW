class Graph:
    def __init__(self, count):
        self.vertices = None * count
        #for i in range(len(V)):
            #self.vertices[i] = 
    
    def __str__(self):
        ret_str = ""
        for vertex in self.vertices:
            ret_str = ret_str + "vertex" + str(vertex) + "\n"
        return ret_str
    
    def add_edges(self, edges):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            current_edge = Edge(u,v,w)
            current_vertex = self.vertices[u]
            current_vertex.edges.append(current_edge)

    
    def bfs (self, source):
        visited = []
        discovered = []   #discovered is a Queue 
        discovered.append(source)

        while len(discovered) > 0:
            u = discovered.pop()
            for vertex in u.edges:
                if vertex not in discovered:
                    discovered.append(vertex)
            visited.append(u)
        
        return visited 
    
    def Depth_First_search(self):
        visited = []
        traverse(self)

        def traverse(Graph):
            for v in range(1, len(Graph)):
                if v not in visited:
                    DFS(v, Graph)

        def DFS(vertex, Graph):
            visited.append(vertex)
            for v in Graph[vertex]:
                if v not in visited:
                    DFS(v, Graph)
        return visited
   
##applied 5 Q9

    def iterative_DFS(Graph, source):
        discovered_stack = []
        discovered_stack.append(source)
        visited = []
        
        while len(discovered_stack) > 0:
            u = discovered_stack.pop()
            if u not in visited:
                visited.append(u)
                for vertex in Graph[u]:
                    if vertex not in visited:
                        discovered_stack.append(len(discovered_stack), vertex)
        


    

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return str(self.u) + " , " + str(self.v) + " , " + str(self.w)
    
class Vertex:
    def __init__(self, id):
        self.id = id

        self.edges = []

        self.discovered = False

        self.visited = False

        self.distance = 0

        self.previous = None

    def __str__(self):
        return str(self.id)

    

if __name__ == "__main__":
    total_vertices = 5
    my_graph = Graph(total_vertices)

    #edges 
    edges = []
    edges.append((3,1,5))
    edges.append((1,2,1))
    edges.append((2,3,-5))
            


