def Bellman_Ford(Graph, source):
    ##loop invariant##
    #At any iteration, dist[v] is no larger than the total weight of the shortest path from s to v 
    #which uses at most i edges
    distances = [float('inf')] * len(Graph)
    pred = [None] * len(Graph)
    distances[source] = 0
    
    for i in range(len(Graph)-1):
        if changes == 1:
            return distances, pred
        for edge in Graph[i]:
            changes = 0
            v = edge.v
            u = edge.u
            w = edge.w
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                pred[v] = u
                changes = 1

    for i in range (len(Graph)):
        for edge in Graph[i]:
            v = edge.v
            u = edge.u
            w = edge.w
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                return ValueError('Negative Cycle')
    
    return distances, pred


def Bellman_Ford2(Graph, source):
    n = len(Graph)
    Dist = [float('inf') for x in Graph]
    Dist[source] = 0
    pred = [None] * n
    

    for i in range(n-1):
        for edge in Graph[i]:
            v = edge.v
            w = edge.w
            u = edge.u
            if Dist[u] != float('inf') and Dist[v] > Dist[u] + w:
                Dist[v] = Dist[u] + w
                pred[v] = u

    for edge in Graph:
        v = edge.v
        w = edge.w
        u = edge.u
        if Dist[u] != float('inf') and Dist[v] > Dist[u] + w:
            Dist[v] = float('-inf')

    return Dist, pred
            


