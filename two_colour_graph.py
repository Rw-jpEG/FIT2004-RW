from collections import deque
from directedgraph import Graph, Edge, Vertex

def two_colourable(Graph, source):
    colour = [-1]*len(Graph)

    visited = deque()

    visited.append(source)
    colour[source] = 0

    while len(visited)>0:
        u = visited.popleft()
        for edge in Graph[u]:
            if edge.v not in visited:
                v = edge.v
                if colour[v] == -1:
                    colour[v] = 1 - colour[u]
                    visited.append[v]
                elif colour[v] == colour[u]:
                    return False
    return True 
    
                
