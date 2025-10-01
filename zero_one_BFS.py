from collections import deque 

def zero_one_BFS(Graph, source, destination):
    dist = [float('inf')]*len(Graph)
    pred = [None]*len(Graph)
    Queue = deque()
    Queue.appendleft(source, 0)
    dist[source] = 0
    while len(Queue)>0:
        u, d = Queue.popleft()
        if d == dist[u]:
            for edge in Graph[u]:
                v = edge.v
                w = edge.w
                if w + dist[u] < dist[v]:
                    dist[v] = w + dist[u]
                    pred[v] = u
                    if w == 0:
                        Queue.appendleft(v, dist[v])
                    else:
                        Queue.append(v, dist[v])

