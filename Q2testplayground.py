
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

########################################################################
# End of module
########################################################################

songs = [
    "cegec",   
    "gcegb",   
    "cdegc"    
]

a = Analyser(songs)


print(a.getFrequentPattern(2))