class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # Each node is its own parent initially
        self.rank = [0] * n                  # Used for union by rank optimization

    def find(self, x):
        """Find the root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y."""
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return False  # Already connected, would form a cycle

        # Union by rank (attach smaller tree under larger tree)
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True
    
def kruskal(n, edges):
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = [] 

    edges.sort()

    for w, u, v in edges:
    #for weight of (u, v) in edges (which are now sorted)
        if uf.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))
        
    return mst_weight, mst_edges 




