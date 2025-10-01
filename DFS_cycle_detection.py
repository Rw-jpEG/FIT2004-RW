from directedgraph import Graph, Edge, Vertex
from collections import deque
import heapq

def DFS_cycle_detection(Graph):

    visited = [-1]*len(Graph)


    def DFS(Graph, source):
        visited[source] = 0
        for edge in Graph[source]:
            v = edge.v
            if visited[v] == 0:
                return True 
            if visited[v] == -1 and DFS(Graph, v):
                return True 
        visited[source] = 1
        return False
            
    for i in range(len(Graph)):
        if visited[i] == -1:
            if DFS(i):
                return True
    return False


def DFS_alg(Graph):
    visited = [-1]*len(Graph)

    def DFS_inner(Graph, source):
        visited[source] = 0
        for edge in Graph[source]:
            v = edge.v
            if visited[v] == -1:
                DFS_inner(Graph, v)
        visited[source] = 1

    for i in range(len(Graph)):
        if visited[i] == -1:
            DFS_inner(Graph, i)
    return visited 
        

def BFS_alg(Graph, source):
    Queue = deque()
    Queue.append(source)
    visited = [-1]*len(Graph)

    while len(Queue)>0:
        u = Queue.popleft()
        visited[u] = 0
        for edge in Graph[u]:
            v = edge.v
            if visited[v] == -1:
                Queue.append(v)
        visited[u] = 1

    return visited

def Dijkstra_alg(Graph, source):
    Queue = heapq()
    heapq.heappush(Queue, source)
    dist = [float('-inf')]*len(Graph)
    dist[source] = 0

    while len(Queue)>0:
        u = heapq.heappop(Queue)
        for edge in Graph[u]:
            v = edge.v
            w = edge.w
            if dist[v] == float('-inf'):
                heapq.heappush(Queue, v)
                dist[v] = dist[u] + w
            elif dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


    

        


    
