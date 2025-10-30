##############################
# MinHeap for Dijkstra
##############################
class MinHeap:
    def __init__(self):
        """
        Function Description:
            initialises a binary min-heap implementation for key, value pairs(priority, value).
            It is used by Dijkstra's to repeatedly get the node with the smallest distance  

        Inputs:
            N/A
        
        Outputs:
            N/A
        
        Time Complexity:
            O(1)

        Aux Space Complexity:
            O(1)
        
        Aux Space Complexity Analysis:
            initialising an empty list uses no additional space
        """
        self.a = []
    
    def __len__(self):
        """
        Function Description:
            returns the length of the heap 

        Inputs:
            N/A
        
        Outputs:
            N/A
        
        Time Complexity:
            O(1)
        
        Time Complexity Analysis:
            Finding the length using pythons len() function is O(1)
        
        Aux Space Complexity:
            O(1)
        
        Aux Space Complexity Analysis:
            finding and returning the length does not require additional space
        """
        return len(self.a)

    def push(self, pair):
        """
        Function Description:    
            Insert a new element into the Min Heap.

        Approach Description:
            -append the new key, value pair to the end of the heap 
            -use the sift_up function to rise the new element to it's correct position.
        
        Inputs:
            pair: a (key, value) tuple to be inserted into the heap

        Outputs:
            N/A
        
        Time Complexity:
            O(logn) where n is the number of elements in the Heap.

        Aux Space Complexity:
            O(1)
        
        Aux Space Complexity Analysis:
            performing arithmetic operations, swaps or other general operations used in the function uses no additional space
        """
        self.a.append(pair)
        self.sift_up(len(self.a) - 1)

    def pop(self):
        """
        Function Description:
            removes and returns the element with the minimum key.
            returns None for an empty heap

        Approach Description:
            -Takes the top (minimum) element and swaps it with the end element which is stored at index(len(heap)). -use the sift_down function to sink the swapped element down to a satisfactory position 
            -return the minimum element.
        
        Inputs:
            self
        
        Outputs:
            top: the minimum element in the heap
        
        Time Complexity:
            O(logn)

        Aux Space Complexity: 
            O(1)  
        
        Aux Space Complexity Analysis:
            performing arithmetic operations, swaps or other general operations used in the function uses no additional space
        """
        if not self.a:
            return None
        if len(self.a) == 1:
            return self.a.pop()
        top = self.a[0]
        self.a[0] = self.a.pop()
        self.sift_down(0)
        return top

    def sift_up(self, i):
        """
        Function Description:
            'rises' an element up to satisfy the min heap property that a parent is smaller than or equal to both of it's children. After function has run, the property will be satisfied for i.

        Approach Description:
            -use a while loop to continually compare if a parent of i is greater than self.a[i]. 
            -If so, swap self.a[i] with its parent. 
            -If not, terminate the while loop
        
        Inputs:
            i: the index of the element to be risen

        Outputs:
            None

        Time Complexity:
            O(logn)

        Aux Space Complexity: 
            O(1)  
        
        Aux Space Complexity Analysis:
            performing arithmetic operations, swaps or other general operations used in the function uses no additional space
        """
        while i>0:
            parent = (i-1)//2
            if self.a[parent][0] <= self.a[i][0]:
                break
            self.a[parent], self.a[i] = self.a[i], self.a[parent]
            i = parent

    def sift_down(self, i):
        """
        Function Description:
            'sinks' an elements down so as to satisfy the Heap property that a parent is smaller than or equal to its children. After the function has run, the Heap will satisfy this property for given node i

        Approach Description:
            -find the indices of the left and right children of i. 
            -While either of the children are smaller than self.a[i], sink self.a[i] down. 
            -If both of its children are greater than i, terminate the while loop.
        
        Inputs:
            i: the index which needs to be sunken down to its correct position

        Outputs:
            No outputs.
        
        Time Complexity:
            O(logn) where n is the number of elements in the heap

        Aux Space Complexity: 
            O(1)
        
        Aux Space Complexity Analysis:
            performing arithmetic operations, swaps or other general operations used in the function uses no additional space
        """
        n = len(self.a)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.a[left][0] < self.a[smallest][0]:
                smallest = left
            if right < n and self.a[right][0] < self.a[smallest][0]:
                smallest = right 
            if smallest == i:
                break
            self.a[smallest], self.a[i] = self.a[i], self.a[smallest]
            i = smallest 

    def decreaseKey(self, value, new_key):
        """
        Function Description:
            Decrease the priority key of the first entry whose value matches the given
            'value'. 
        
        Approach Description:
            -initialises an index variable to -1. 
            -iterate through the heap to find the corresponding value and save the index
            -update the key for the saved index 
            -use the sift_up function to find the correct position given the new key

        Inputs:
            value: value of the node that needs to have its key decreased
            new_key: new key value to replace the old key
        
        Outputs:
            None

        Time Complexity:
            O(n) where n is the number of elements in the heap

        Aux Space Complexity:
            O(1)

        Aux Space Complexity Analysis:
            performing arithmetic operations, swaps or other general operations used in the function uses no additional space
        """
        index = -1
        for i in range(len(self)-1):
            if self.a[i][1] == value:
                index = i
                break
        if index == -1:
            return 
        self.a[index] = (new_key, value)
        self.sift_up(index)

    def printHeap(self):
        """
        Function Description:
            prints the heap
        
        Approach Description:
            -use a print statement to print self.a

        Inputs:
            N/A

        Outputs:
            prints self.a

        Time Complexity:
            O(1)
        
        Aux Space Complexity:
            O(1)
        
        Aux Space Complexity Analysis:
            printing uses no additional space
        """
        print("Min Heap:", self.a)

##############################
# Dijkstra using MinHeap
##############################
def Dijkstra_alg(L, adj, src):
    """
    Function Description:
        Single source shortest path problem which finds the shortest distance to all vertices in a graph
        with non-negative weights. This implementation uses the Min Heap class.

    Input:
        L: the number of locations 
        adj: The Graph in adjacency list form
        src: the desired source node
    
    Output:
        dist: array of shortest distances from the source node to all other vertices

    Time Complexity:
        O(RlogL) where R represents the roads in the city that connect locations and L represents locations

    Aux Space Complexity:
        O(L) 
    
    Aux Space Complexity Analysis:
        for storing distance array
    """
    dist = [float('inf')] * L
    dist[src] = 0
    heap = MinHeap()
    heap.push((0, src))
    while len(heap) > 0:
        item = heap.pop()
        if item is None:
            break
        d = item[0]
        u = item[1]
        if d != dist[u]:
            continue
        for edge in adj[u]:
            v = edge[0]
            w = edge[1]
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heap.push((nd, v))
    return dist

def encode_state(bus_counts, factors):
    """
    Function Description:
        Encodes bus counts into a single integer state as tuples or multi-dimensional dp array is infeasible
    
    Approach Description:
        -Each bus has its own "base" = max_capacity + 1, stored in the factors array
        -The state can be computed as state = sum(bus_counts[i] * multiplier_i)
        -multiplier_i is the product: factors[0] * factors[1] * ... * factors[i-1]
        -creates an integer representation of a particular configuration of buses 

    
    Inputs:
        bus_counts: list of integers representing the current amount of students on the bus of the corresponding index
        factors: list of integers where factors[i] = max_capacity[i] + 1

    Outputs:
        state: integer representing an encoded bus configuration
    
    Time Complexity:
        O(B)
    
    Time Complexity Analysis:
        The function iterates through each of the B buses once, performing constant-time
        arithmetic operations (multiplication and addition) for each bus

    Aux Space Complexity:
        O(1)

    Aux Space Complexity Analysis:
        Only uses a constant amount of extra space for the state.
    """
    state = 0
    multiplier = 1
    for i in range(len(bus_counts)):
        state += bus_counts[i] * multiplier
        multiplier *= factors[i]
    return state

def decode_state(state, factors, B):
    """
    Function Description:
        Decodes an integer state back to bus counts

    Approach Description:
        -Uses repeated modulus and integer division to extract each bus count
        -For each bus i, the count is state % by factors[i] (to get the digit)
        -Then state = state // factors[i] (remove that digit)
        -Process repeats for all buses to reconstruct the original counts

    
    Inputs:
        state: an single integer representing bus counts
        factors: a list of integers where factors[i] = max_capacity[i] + 1 for bus[i]
        B; number of buses 
    
    Outputs:
        bus_counts: a list of integers where bus_counts[i] represents the number of students on bus[i]

    Time Complexity:
        O(B)

    Time Complexity Analysis:
        The function iterates through each of the B buses once, performing constant-time
        modulus and division operations for each bus

    Aux Space Complexity:
        O(B)

    Aux Space Complexity Analysis:
        creates a new bus_counts to store each buses number of students
    """
    bus_counts = [0] * B
    for i in range(B):
        bus_counts[i] = state % factors[i] 
        state //= factors[i]
    return bus_counts


##############################
# Main assignment function
##############################
def assign(L, roads, students, buses, D, T):
    """
    Function Description:
        Determines an allocation of students to buses so that the buses can transport exactly T students.
        -Each bus must be used
        -Each bus has a min and max amount of students it can transport
        -Each student can only be assigned to one bus
        -Each student s is only assigned to a pickup point which is within distance D of the location of s

    Approach Description:
        -Precompute shortest distances from all locations to bus pickup points using Dijkstra 
        -Get the pickup locations for the adjacency list and buses
        -Run Dijkstra's on the pickup locations for each pickup location
        -For each student, find the list of reachable bus locations
        -Use dynamic programming:
            -the optimal substructure exists here because an optimal assignment of a subset of students can be used to construct an optimal asignment for all students (assignment for n students can be used to get the optimal assignment for n + 1 students)
            -The overlapping subproblems occur when different sequences of student assignments lead to identical bus count configurations.
        -develop memoisation table where dp[i][state] represents whether we can use the first i students to achieve a bus configuration state 'state'.
            -Bus configuration state can take on the form of an array of length b where each element represents the corresponding bus of that index and the value at that index represents the number of students travelling on that bus
        -Fill out DP table 
        -use the decode state helper functions to turn the placeholder integers back into assignments of students to buses
    
    Inputs:
        - L: number of locations (0..L-1)
        - roads: list of (u, v, w) undirected roads
        - students: list of length S, student i located at students[i]
        - buses: list of B tuples (pickup_loc, min_cap, max_cap)
        - D: maximum distance students are willing to travel
        - T: exact total number of students to transport

    Outputs:
        - list of length S, where element i is bus index (0..B-1) assigned to student i, or -1 if not assigned.
        - returns None if no feasible assignment exists.
    
    Time Complexity:
        O(S*T + L + RlogL) where S is the length of students, T is the exact number of students needed to be transported, L is the number of locations and R is the number of roads.
            -Dijkstra's: O(B*(RlogL)) for B = 18 pickup locations which is constant so can be simplified to O(RlogL)
            -Building Graph Adjacency List: O(L + R)
            -DP: O(S*T*2^B), again since B is constant and using binary state representation we can simplify to O(S*T) 

    Aux Space Complexity:
        O(S + L + R)
    
    Aux Space Complexity Analysis:
        -Constructing the Graph requires O(L+R) additional space complexity
        -Distance Matrix derived from the Dijkstra's from each bus location takes up O(L*B); since B <= 18 we can simplify this to O(L)
        -DP memo table: O(S*state) where state is the product of all (max capacities + 1) of buses. (If we had 3 buses with max capacities (2,3,4); the state size would be (2+1)*(3+1)*(4+1) = 60). Since there can only be a maximum of 18 factors so state size will always be constant if we know B, therefore O(S). 
    """

    #create adjacency list representation of roads and locations
    graph = [[] for _ in range(L)]
    for u, v, w in roads:
        #for each edge (assuming two way travel) add the directed edge from u to v and v to u
        graph[u].append((v,w))
        graph[v].append((u,w))

    B = len(buses)
    S = len(students)

    #precompute distances from each bus location to all other locations
    bus_locations = [bus[0] for bus in buses]
    dist_from_buses = []

    for source in bus_locations:
        #run Dijkstra's to compute the shortest distance for each bus location to all other locations
        dist = Dijkstra_alg(L, graph, source)
        dist_from_buses.append(dist)

    #Find which students are 'willing to travel' to which buses by using their locations and a radius of D to bus locations 
    student_bus_match = [[] for _ in range(S)]
    for stud_index in range(S):
        stud_loc = students[stud_index]
        for bus_index in range(B):
            if dist_from_buses[bus_index][stud_loc] <= D:
                student_bus_match[stud_index].append(bus_index)

    #Find min and max students and check feasibility for early exit
    #min number of students that must be collected
    total_min = sum(bus[1] for bus in buses)

    #maximum number of students that can be collected
    total_max = sum(bus[2] for bus in buses)

    #count reachable students, add 1 for a student if they have at least one viable location
    reachable_students = sum(1 for match in student_bus_match if match)

    if T<total_min or T>total_max or reachable_students<T:
        return None
    
    #store capacities
    max_cap = [bus[2] for bus in buses]
    low_bound = [bus[1] for bus in buses]

    #encode bus counts as base (max_cap + 1)
    state_factors = [cap + 1 for cap in max_cap]
    state_size = 1
    for factor in state_factors:
        state_size *= factor

    #set up DP table where dp[student_idx][state] = assignment decision or None for non valid students 
    dp = [[None] * state_size for _ in range(S + 1)]

    #base case: after processing all students 
    for state in range(state_size):
        bus_counts = decode_state(state, state_factors, B)

        total_assigned = sum(bus_counts)
        if total_assigned == T:
            valid = True
            for i in range(B):
                if not (buses[i][1] <= bus_counts[i] <= buses[i][2]):
                    valid = False
                    break

            if valid:
                #fill in DP table for student 
                dp[S][state] = -2 #where -2 indicates a valid state

    #Fill in DP table starting from the end 
    for stud_index in range(S-1, -1, -1):
        for state in range(state_size):
            if dp[stud_index + 1][state] is not None:
                dp[stud_index][state] = -1
            
            current_bus_counts = decode_state(state, state_factors, B)
            total_assigned = sum(current_bus_counts)
    
            if total_assigned < T:
                for bus_index in student_bus_match[stud_index]:
                    if current_bus_counts[bus_index] < max_cap[bus_index] and total_assigned + 1 <= T:
                        new_bus_counts = current_bus_counts.copy()
                        #add one to the new bus count for this bus index since it is valid (doesnt go over capacity) and we still have room for assignments
                        new_bus_counts[bus_index] += 1
                        next_state = encode_state(new_bus_counts, state_factors)

                        if dp[stud_index + 1][next_state] is not None:
                            dp[stud_index][state] = bus_index
                            break #found a valid assignment 

    
    #initialise student assignments to -1 for unassigned and counts to 0
    initial_state = encode_state([0] * B, state_factors)
    if dp[0][initial_state] is None:
        return None   
    
    assignment = [-1] * S
    
    current_state = initial_state

    for stud_index in range(S):
        decision = dp[stud_index][current_state]
        if decision == -1:
            # Student not assigned, state remains the same
            assignment[stud_index] = -1
        else:
            # Student assigned to a bus
            assignment[stud_index] = decision
            current_counts = decode_state(current_state, state_factors, B)
            current_counts[decision] += 1
            current_state = encode_state(current_counts, state_factors)

    return assignment  



#--------------------#
#Q2
#--------------------#

def note_to_int(ch):
    """
    Function Description:
        Converts a single musical note character into an integer, allowing interval differences to be computed numerically.
    
    Inputs:
        ch: a single character to be converted into an inteer
    
    Outputs:
        Integer value equal to ord(ch) - ord('a')
    
    Time complexity:
        O(1) 
    
    Aux Space Complexity:
        O(1)
    
    Aux Space Complexity Analysis:
        Arithmetic operations require no additional space
    """
    return ord(ch)-ord('a')

def compute_intervals(seq):
    """
    Function Description:
        turns a sequence string into a list of ordered intervals.
    
    Approach Description:
        -if the length of the sequence is 1 or less then return an empty list, since there are no possible 'intervals'. 
        -Otherwise, create an array which stores the computed difference of every element minus its previous neighbour 
    
    Inputs:
        seq: a string containing a sequence of notes

    Outputs:
        intervals: a list of interval differences between every pair of neighbouring notes in seq
    
    Time Complexity:
        O(n) where n is the length of seq
    
    Aux Space Complexity:
        O(n) 
    
    Aux Space Complexity Analysis:
        need to store the list of interval differences which needs O(n) space.
    """
    n = len(seq)
    if n <= 1:
        return []
    arr = [note_to_int(c) for c in seq]
    intervals = []
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        intervals.append(diff)
    return intervals  

class TrieNode:
    def __init__(self, num_songs):
        """
        Function Description:
            initialises a Trie node class for intervals. children indexed by interval + 25 (range 0..51).

        Inputs:
            num_songs: the number of songs in the record companies song index

        Outputs:
            N/A

        Time Complexity:
            O(num_songs) for song_seen array initialisation

        Aux Space Complexity:
            O(num_songs) 
        
        Aux Space Complexity Analysis:
            storing song_seen array requires O(num_songs) aux space complexity
        """
        self.children = [None]*52 #-25 to 25 possible intervals. Think about a music system with 25 tone equal temprement 
        self.freq = 0
        self.song_seen = [False]*num_songs 
        self.song_occurrences = []

class IntervalTrie:
    def __init__(self, num_songs):
        """
        Function Description:
            initialises an IntervalTrie class which inserts suffixes of interval sequences and count distinct songs with each pattern

        Inputs:
            num_songs: number of songs 

        Outputs:
            N/A

        Time Complexity:
            O(num_songs) for TrieNode creation

        Aux Space Complexity:
            O(num_songs)
        
        Aux Space Complexity Analysis:
            TrieNode initiation requires O(num_songs) additional storage
        """
        self.root = TrieNode(num_songs)
        self.num_songs = num_songs 
    
    def insert_suffixes(self, intervals, song_index):
        """
        Function Description:
            insert each of the suffixes of one song's interval sequence into the Trie. Mark nodes so that any 
            song can only contribute any given pattern only once
        
        Approach Description:
            -build all substrings of a given interval list by setting some i as the root and iterating it to 
            find all the substrings from i to m. 
            -Eliminate any negative intervals by shifting all interval differences up 25. 
            -Check, for each substring, whether or not the substring exists in the Trie already and if so, update the pattern frequency 

        Inputs:
            intervals: list of intervals contained in one song
            song_index: identifier for the given song
        
        Outputs:
            N/A
        
        Time Complexity:
            O(m^2) where m is the length of the given interval list.
        
        Aux Space Complexity:
            O(m²) 
        
        Aux Space Complexity Analysis:
            the space complexity here is across all insertions, as new TrieNodes are created for unique substrings. Per function call, additional space is O(1).
        """
        m = len(intervals)
        for i in range(m):
            node = self.root 
            #Build all substrings from position i to m
            for j in range(i, m):
                diff = intervals[j]
                idx = diff + 25 #we need to eliminate any negative intervals eg. -25 (from z to a)
                if node.children[idx] is None:
                    node.children[idx] = TrieNode(self.num_songs)
                node = node.children[idx]
                if not node.song_seen[song_index]:
                    node.song_seen[song_index] = True 
                    #increase the frequency of songs with this prefix
                    node.freq += 1
                    #record the song where this pattern occurs
                    node.song_occurrences.append((song_index, i))

class Analyser:
    """
    Class Description:
        Build interval trie for a list of note sequences and query most frequent pattern of length K.
    """
    def __init__(self, sequences):
        """
        Function Description:
            Preprocess and build the interval tree given the note sequences

        Input:
            sequences: list of note sequences (can be converted to intervals), each element of the list is a string of note sequences for one song
        
        Time Complexity:
            O(N * M^2) where N is the number of songs and M is the length of the interval list for the song

        Aux Space Complexity:
            O(N * M^2)
        
        Aux Space Complexity Analysis:
            in the worst case, the Trie may contain O(M²) nodes per song, giving total Trie storage of O(N * M²) across all songs. Each interval list also has length up to M (where M is the number of notes in the song), so the total storage required for all interval lists is O(N * M). But this is dominated by the Trie storage
        """
        self.sequences = sequences
        self.N = len(sequences)
        self.trie = IntervalTrie(self.N)
        self.max_len = 0

        #preprocess all songs into respective interval lists 
        self.intervals = []
        for song_index in range(self.N):
            seq = sequences[song_index]
            song_interval = compute_intervals(seq)
            self.intervals.append(song_interval)
            if len(song_interval) > self.max_len:
                self.max_len = len(song_interval)
            #insert song into the Trie
            self.trie.insert_suffixes(song_interval, song_index)

    def DFS_k(self, node, depth, k, path, best):
        """
        Function Description:
            specific depth first search up to given k value which traverses the graph and returns the most frequent pattern of length k
        
        Approach Description:
            -given a node, iterate over all its possible children (all possible intervals). 
            -If any children exist, add them to the path and recursively call the DFS function 
            -pop the current element from the path. 
            -Check at the start of each function call whether we have reached a depth of k 
            -if so take note of the best patterns frequency and the intervals of the pattern.
        
        Inputs:
            node: current TrieNode
            depth: current depth in trie
            K: target pattern length
            path: current interval sequence
            best: list [best_freq, best_pattern]

        Outputs:
            N/A
        
        Time Complexity:
            O(min(52^k, N) since each node can have potentially 52 children but in reality most of the children are actually none, so generally the worst case time complexity will be O(N) where N is the number of nodes reachable up to depth k. O(52^k) would only occur if every single note had a child of every potential interval.

        Aux Space Complexity:
            O(k)
        
        Aux Space Complexity Analysis:
            path may be extended up to length k leading to additional O(k) space. DFS also uses a recursion stack which may reach O(k) Aux space complexity
        """
        if node is None:
            return 
        
        if depth == k:
            #reached the target length paths 
            if node.freq>best[0]:
                best[0] = node.freq
                best[1] = path[:]
                best[2] = node.song_occurrences
            return 
        
        #continue DFS for all possible interval children 
        for i in range(52):
            child = node.children[i]
            if child is not None:
                path.append(i-25)
                self.DFS_k(child, depth+1, k, path, best)
                path.pop()

    def getFrequentPattern(self, K):
        """
        Function Description:
            for a given pattern length of K, finds the most frequent interval pattern of length K from a list of songs. 
        
        Approach Description:
            -check if K is a feasible value to find intervals for 
            -if so, run DFS on the Trie containing all songs to find the most frequent pattern of length K and its frequency. 
            -Convert the intervals derived from the Trie back into notes.
        
        Inputs:
            K: pattern length to search for

        Outputs:
            notes: the notes of the most frequent pattern in the 'key' of 'a', that is, we are treating the first note of the pattern as 'a' but it could be transposed to match with any of the songs it is found in which may have different keys.

        Time Complexity:
            O(N + k) where N is the number of Trie nodes explored up to depth k (the DFS cost), and k accounts for interval-to-note conversion
        
        Aux Space Complexity:
            O(k) where k is the length of patterns
        
        Aux Space Complexity Analysis:
            we need to store at least the intervals/notes in the optimal path (which is length k)
        """
        if K<1 or K>self.max_len:
            return []   
        
        best = [0, [], []]  # [freq, intervals, song_occurrences]
    
        self.DFS_k(self.trie.root, 0, K, [], best)

        if best[0] == 0:
            return None
        
        if best[2]:
            #use first occurrence of a song using frequent pattern
            song_index, start_pos = best[2][0]
            song = self.sequences[song_index]

            pattern_notes = []
            for i in range(K + 1):
                if start_pos + i < len(song): #use start_pos to start from the start of the pattern 
                    #if the current note in the song is valid append it to the notes array.
                    pattern_notes.append(song[start_pos + i])

            return pattern_notes