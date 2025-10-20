from directedgraph import Graph, Edge, Vertex


class MinHeap:
    def __init__(self):
        self.a = []

    """Insert a new element into the Min Heap."""
    def insert(self, tup_val):
        self.a.append(tup_val)
        i = len(self.a) - 1
        while i > 0:
            parent = self.a[(i - 1) // 2] 
            if self.a[parent][1] > self.a[i][1]:
                self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
                i = (i - 1) // 2

    """Delete a specific element from the Min Heap."""
    def delete(self, val):
        i = -1
        for j in range(len(self.a)):
            if self.a[j][0] == val:
                i = j
                break
        if i == -1:
            return
        self.a[i] = self.a[-1]
        self.a.pop()
        
        self.minHeapify(i, len(self.a))

    """Heapify function to maintain the heap property.""" 
    def minHeapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            if self.a[left][1] < self.a[smallest][1]:
                smallest = left
        if right < n:
            if self.a[right][1] < self.a[smallest][1]:
                smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.minHeapify(smallest, n)

    """Search for an element in the Min Heap."""
    def search(self, element):
        for j in self.a[0]:
            if j == element:
                return True
        return False

    def getMin(self):
        minimum = self.a[0]
        self.a[0], self.a[len(self)] = self.a[len(self)], self.a[0]
        self.delete(self.a[len(self)][0])
        return minimum 
    
    def printHeap(self):
        print("Min Heap:", self.a)

    def decreaseKey(self, value, new_key):
    
        i = -1
        for j in range(len(self.a)):
            if self.a[j][0] == value:
                i = j
                break
        if i == -1:
            return  # not found

        # update key
        self.a[i] = (value, new_key)

        # bubble up to restore heap property
        while i > 0:
            parent = (i - 1) // 2
            if self.a[parent][1] > self.a[i][1]:
                self.a[i], self.a[parent] = self.a[parent], self.a[i]
                i = parent
            else:
                break



def Dijkstra_alg(Graph: Graph, source):
    Heap = MinHeap()
    distance = []*len(Graph)

    
    for vertex in Graph:
        if vertex == source:
            Heap.insert(vertex)
            distance[source] = 0
    
    while len(Heap)>0:
        u = Heap.getMin()
        for edge in Graph[u]:
            v = edge.v
            w = edge.w
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                Heap.insert(vertex)
    
    return distance
        
        



