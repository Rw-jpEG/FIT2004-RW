def non_recursive_DFS(Graph, source):
    visited = []
    stack = []
    stack.push(source)
    while len(stack)>0:
        u = stack.pop()
        for edge in Graph[u]:
            v = edge.v
            if v not in visited:
                stack.push(v)
    return visited
