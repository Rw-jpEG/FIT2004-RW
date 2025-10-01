def pure_cycles(Graph):

    visited = [False]*len(Graph)
    num_components = 0

    def DFS(u):
        stack = [u]
        vertices = 0
        edges = 0
        is_cycle = True

        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            vertices += 1

            # Check degree
            if len(Graph[node]) != 2:
                is_cycle = False

            for v in Graph[node]:
                edges += 1  # count each edge direction
                if not visited[v]:
                    stack.append(v)

        # For undirected graph, edges are counted twice
        edges //= 2

        # A pure cycle must have V = E and all nodes degree 2
        return is_cycle and edges == vertices

    for v in range(len(Graph)):
        if not visited[v]:
            if DFS(v):
                num_components += 1

    return num_components
        
