from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Adds an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the item from the front of the queue."""
        if self.is_empty():
            return "Queue is empty"
        return self.items.popleft()

    def peek(self):
        """Returns the item at the front of the queue without removing it."""
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.items)


def reachable_vertices(graph: deque, s):
    #s is the source vertex
    visited = []
    visited.append(s)

    queue = Queue()
    queue.push(s)

    while not queue.is_empty():
        u = queue.pop()
        for v in graph[u]:
            if v not in visited:
                visited.append(v) 
                queue.push(v)
    
    return visited
        

