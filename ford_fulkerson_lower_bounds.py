class Edge:
    def __init__(self, v, capacity, lower_bound):
        self.v = v
        self.capacity = capacity
        self.lowerbound = lower_bound
        self.rev = None


class Ford_Fulkerson_Graph:

    def __init__(self, size):
        self.adj = [[] for _ in range(size)]
        self.size = size
        self.vertex_demand = [0] * size

    def add_edge(self, u, v, capacity, lowerbound):
        forward = Edge(v, capacity)
        reverse = Edge(u, 0)
        forward.rev = reverse
        reverse.rev = forward
        self.adj[u].append(forward)
        self.adj[v].append(reverse)

    def add_vertex_demand(self, vertex, demand):
        if 0 <= vertex < self.size:
            self.vertex_demand[vertex] = demand


    def _dfs(self, u, sink, visited, parent):
        visited[u] = True
        if u == sink:
            return True

        for edge in self.adj[u]:
            v = edge.v
            cap = edge.capacity
            if not visited[v] and cap > 0:
                parent[v] = (u, edge)
                if self._dfs(v, sink, visited, parent):
                    return True
        return False


    def ford_fulkerson_lb(self, source, sink):
        """ford fulkerson algorithm to solve flow problems with lower bounds and circlation of demands"""
        max_flow = 0
        visited = [False]*self.size
        parent = [None]*self.size

        path = self._dfs(source, sink, visited, parent)

        while path:
            path_flow = float('inf')
            v = sink
            while v != source:
                #find bottleneck
                u, edge = parent[v]
                path_flow = min(path_flow, edge.capacity)
                v = u

            v = sink
            while v != source:
                #update residual capacities
                u, edge = parent[v]
                edge.capacity -= path_flow
                edge.rev.capacity += path_flow 
                v = u
            
            max_flow += path_flow

            visited = [False]*len(self)
            parent = [None]*len(self)
            path = self._dfs(source, sink, visited, parent)

        return self, max_flow

    def lower_bounds_demands(self, source, sink):
        
        super_source = self.size
        super_sink = self.size + 1
        new_graph = Ford_Fulkerson_Graph(self.size + 2)
        new_graph.adj = [lst.copy() for lst in self.adj]
        new_graph.vertex_demand = self.vertex_demand.copy()

        if not new_graph.vertex_demand:
            for v in range(1, self.size-1):
                new_graph.vertex_demand[v] = 0

        for u in range(self.size):
            for edge in self.adj[u]:
                if edge.lowerbound > 0:
                    new_graph.vertex_demand[u] -= edge.lowerbound
                    new_graph.vertex_demand[v] += edge.lowerbound 
                    edge.capacity -= edge.lowerbound 

        total_demand = 0
        for vertex in range(self.size):
            if new_graph.vertex_demand[v] > 0:
                new_graph.add_edge(super_source, vertex, new_graph.vertex_demand[v])
                total_demand += new_graph.vertex_demand[v]
            elif new_graph.vertex_demand[v] < 0:
                new_graph.add_edge(vertex, super_sink, -(new_graph.vertex_demand[v]))

        flow = new_graph.ford_fulkerson_lb(super_source, super_sink)
        feasible = flow == total_demand

        return new_graph, feasible


            
            
            




            
                
        