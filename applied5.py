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





visited = []


def traverse(Graph):
    for v in range(1, len(Graph)):
        if v not in visited:
            DFS(v, Graph)

def DFS(vertex, Graph):
    visited.append(vertex)
    for v in Graph[vertex]:
        if v not in visited:
            DFS(v, Graph)

#for question 1 we can modify the depth first search 

colour = {}


def traverse_colour(Graph):
    for v in range(1, len(Graph)):
        if v not in visited:
            DFS_colour(v, Graph, 1)

def DFS_colour(vertex, Graph, colour = 1):
    colour[vertex] = colour 
    for v in Graph[vertex]:
        if v not in visited:
            if colour == 1:
                DFS_colour(v, Graph, colour-1)
            elif colour == 0:
                DFS_colour(v, Graph, colour+1)


visited_cycles = []
#to implement a cycle checker for a directed graph, the difference largely lies in the storage 

def has_cycle(graph):
    state = {v: 0 for v in graph} #0=unvisited, 1=visiting, 2=visited

    def traverse_directed_cycle(Graph):
        for v in range(1, len(Graph)):
            if v not in visited:
                DFS_directed_cycle(v, Graph)

    def DFS_directed_cycle(vertex, Graph):
        state[vertex] = 1
        for v in Graph[vertex]:
            if v == 0 and DFS_directed_cycle(v, Graph):
                return True
            if v == 1:
                return True 
            else:
                return False
        for v in graph:
            if state[v] == 0:
                if DFS_directed_cycle(v, Graph):
                    return True 
        return False
            

def Breadth_first_colour(graph, source):
    
    colours = {}
    
    visited = Queue()
    colours[source] = "Black"
    visited.append(source)
    while len(visited) > 0:
        u = visited.pop()
        for v in graph[u]:
            if v not in visited:
                if colours[u] == "Black":
                    colours[v] = "Red"
                else:
                    colours[v] = "Black" 
                visited.push(v)
            else:
                return False


def Depth_first_cycle_detection(graph, source):

    visited = {v: None for v in graph}

    def traverse_cycle_detection(graph):
        for v in range(1, len(graph)):
            if visited[v] is None:
                if DFS_first_cycle_detection(graph, v):
                    return True 
        return False 


    def DFS_first_cycle_detection(graph, vertex):
        visited[vertex] = "Visiting"
        for v in graph[vertex]:
            if visited[v] == None and DFS_first_cycle_detection(graph, v):
                return True
            elif visited[v] == "Visiting":
                return True
        visited[v] = "Visited"
        return False 
        


def pure_cycles(Graph):

    def Breadth_cycles(graph, source):
        discovered = []     
        i = 0
        discovered.append(source)

        while discovered[i] != discovered[0]:
            i += 1
            if len(Graph[i])>1:
                return ValueError("not pure cycle")
            for v in Graph[i]:
                discovered.append(v)
        
        return i


                
           
                    
