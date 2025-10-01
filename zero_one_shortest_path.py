from applied5 import Queue

def Breadth_first_colour(graph, source):
    
    visited = Queue()
    visited.append(source)
    while len(visited) > 0:
        u = visited.pop()
        for edge in graph[u]:
            if edge.w == 0:
                if edge not in visited:
                    visited.append(edge)
            visited.append(edge)
                
            