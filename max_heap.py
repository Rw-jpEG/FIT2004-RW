class MaxHeap:
    def __init__(self):
        self.a = []   # internal array to store heap

    def __len__(self):
        return len(self.a)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        """Insert a new key into the max heap."""
        self.a.append(key)
        i = len(self.a) - 1
        # Bubble up
        while i > 0 and self.a[self.parent(i)] < self.a[i]:
            self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
            i = self.parent(i)

    def maxHeapify(self, i):
        """Restore max-heap property from index i downward."""
        n = len(self.a)
        largest = i
        l, r = self.left(i), self.right(i)

        if l < n and self.a[l] > self.a[largest]:
            largest = l
        if r < n and self.a[r] > self.a[largest]:
            largest = r

        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.maxHeapify(largest)

    def extractMax(self):
        """Remove and return the maximum element."""
        if not self.a:
            return None
        if len(self.a) == 1:
            return self.a.pop()

        root = self.a[0]
        self.a[0] = self.a.pop()  # move last to root
        self.maxHeapify(0)
        return root

    def getMax(self):
        """Return maximum element without removing it."""
        return self.a[0] if self.a else None

    def delete(self, i):
        """Delete element at index i."""
        if i < 0 or i >= len(self.a):
            return
        # Move element to infinity and bubble up
        self.a[i] = float("inf")
        while i > 0 and self.a[self.parent(i)] < self.a[i]:
            self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
            i = self.parent(i)
        self.extractMax()

    def printHeap(self):
        print("Max Heap:", self.a)
