from directedgraph import Graph, Edge, Vertex
from collections import deque

def BFS_cycle(graph: Graph, source):
    visited = [-1]*len(graph)

    dist = []

    queue = deque()

    queue.append(source)
    dist[source] = 0

    while len(queue)>0:
        u = queue.popleft()
        visited[u] = 0
        for edge in Graph[u]:
            v = edge.v
            w = edge.w
            if visited[v] == 0:
                return dist[v]
            elif visited[v] == -1:
                queue.append(v)
                dist[v] = dist[u] + w
            elif visited[v] == 1:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        visited[u] = 1
    
    return False

def shortest_cycle(graph: Graph):
    cycle_lengths = []

    for vertex in graph:
        result = BFS_cycle(graph, vertex)
        if result != False:
            cycle_lengths.append(result)
    
    return min(cycle_lengths)

    