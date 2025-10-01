def Floyd_Warshall(Graph):
    V = len(Graph)
    dist =[[float('inf')] * V for  x in V]

    for i in range(V):
        for j in range(V):
            dist[i][j] = Graph[i][j]
    
    # Distance to self is zero
    for i in range(V):
        dist[i][i] = 0

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def Floyd_Warshall2(Graph):
    n = len(Graph)
    dist = [[float('inf')]*n for x in Graph]

    for i in range(n):
        dist[i][i] = 0

    for i in range(n):
        for edge in Graph[i]:
            v = edge.v
            u = edge.u
            w = edge.w
            dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    for i in range(n):
        if dist[i][i] < 0:
            print('negative cycle detected at vertex', i)
    
    return dist