
from collections import deque

def bfs(Graph, source):
    visited = [-1]*len(Graph)
    Q = deque() 
    Q.append(source)
    pred = [None]*len(Graph )


    while len(Q)>0:
        u = Q.pop()
        for edge in Graph[u]:
            v = edge.v
            w = edge.w
            if visited[v] == -1:
                Q.append(v)
                pred[v] = u
            visited[u] = 1
    return visited, pred

def dfs(Graph, source, visited, parent ):
    visited[source] = 0
    for edge in Graph[source]:
        v = edge.v
        if visited[v] == -1:
            dfs(Graph, v)
            parent[v] = source
    visited[source] = 1

def ford_fulkerson_bfs(Network, source, sink):
    parent = [-1]*len(Network)
    max_flow = 0

    while bfs(Network, source):
        bfs_res, parent = bfs(Network, source)
        path_flow = float('-inf')
        s = source
        while s != source:
            path_flow = min(path_flow, Network[parent[s]][s])
            s = parent[s]
    
        max_flow += path_flow 
        v = sink

        while v != source:
            u = parent[v]
            Network[u][v] -= path_flow
            Network[v][u] += path_flow
            v = parent[v]

    return max_flow


def Ford_fulkerson_dfs(Network, source, sink):
    parent = [-1]*len(Network)
    max_flow = 0

    while True:
        visited = [False]*len(Network)
        if not dfs(Network, source, sink, parent, visited):
            break
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, Network[u][v])
            v = parent[v]
        
        max_flow += path_flow

        v = sink
        
        while v!=source:
            u = parent[v]
            Network[u][v] -= path_flow
            Network[v][u] += path_flow
            v = parent[v]
    
    return max_flow 

