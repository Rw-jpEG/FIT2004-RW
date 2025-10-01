from array import array


def salesman(houses:array):
    memo = [None]*(len(houses) + 1)
    memo[0] = 0
    memo[1] = houses[0]
    choice = [None]*(len(houses) + 1)

    for i in range(2, len(houses)+1):
        # for house in houses:
        memo[i] = max(houses[i-1] + memo[i-2], memo[i-1])
        
        
    pred = []
    pred.append(max(memo[len(memo)-1], memo[len(memo)-2]))

    i = len(memo) - 1
    while i >= 2:
        if memo[i] != memo[i-1]:
            pred.append(i-2)
            i -= 2
        else:
            pred.append(i-1)
            i -= 1
    return memo[len(houses)], reversed(pred)

houses = [50, 10, 12, 65, 40, 95, 100, 12, 20, 30]
total, order = salesman(houses)




def maze(Grid):
    memo = [[0 for _ in range(len(Grid[0]))] for _ in range(len(Grid))]
    memo[-1][-1] = 1

    for i in range(len(Grid)-1, -1, -1):
        for j in range(len(Grid[0])-1, -1, -1):
            # if j==0 and i==len(Grid):
            #     return memo[i][j]
            # else:
            #     memo[i][j] = memo[i-1][j] + memo[i][j+1]
            # cell is blocked:
            if Grid[i][j]:
                memo[i][j] = 0
            # we're at the far right side:
            elif j == len(Grid)-1 and i < len(Grid)-1:
                memo[i][j] = memo[i+1][j]
            # we're at the bottom
            elif i == len(Grid)-1 and j < len(Grid)-1:
                memo[i][j] = memo[i][j+1]
            # general case:
            elif i < len(Grid)-1 and j < len(Grid)-1:
                memo[i][j] = memo[i+1][j] + memo[i][j+1]
    return memo

def money_maze(Grid):
    memo = [[0 for _ in range(len(Grid[0]))] for _ in range(len(Grid))]
    memo[-1][-1] = Grid[0][0]

    for i in range(len(Grid)-1, -1, -1):
        for j in range(len(Grid[0])-1, -1, -1):
            # we're at the far right side:
            if j == len(Grid)-1 and i < len(Grid)-1:
                memo[i][j] = Grid[i][j] + memo[i-1][j]

            # we're at the bottom
            elif i == len(Grid)-1 and j < len(Grid)-1:
                memo[i][j] = Grid[i][j] + memo[i][j-1]

            # general case:
            elif i < len(Grid)-1 and j < len(Grid)-1:
                memo[i][j] = Grid[i][j] + max(memo[i-1][j], memo[i][j-1])

    return memo

def longest_substring(arr):
    
    n = len(arr)
    # memo[i] = length of LIS ending at index i
    memo = [1] * n  
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                memo[i] = max(memo[i], memo[j] + 1)
    
    return max(memo) 

def longest_common_sequenc(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    memo = [[0]*(m+1) for _ in (n+1)]

    for i in range(n):
        for j in range(m):
            if arr1[i-1] == arr2[j-1]:
                memo[i][j] = 1 + memo[i-1][j-1]
            else:
                memo[i][j] = max(memo[i][j-1], memo[i-1][j])

    return max(memo)

def largest_continuous_sum(arr):
    n = len(arr)
    max_sum = float('-inf')
    max_subsequence = []

    for i in range(n):
        current_sum = 0
        current_array = []
        for j in range(i, n):
            current_sum += arr[j]
            current_array.append(arr[j])
            if current_sum > max_sum:
                max_subsequence = current_array
                max_sum = current_sum
            


    return max_sum, max_subsequence
            


def Kadane_alg(arr):
    n = len(arr)
    global_max = float('-inf')
    current_max = 0

    for i in range(n):

        global_max = max(current_max, global_max)


def street_stones(arr_l, arr_r):
    n = len(arr_l)

    dp_left = [0] * n
    dp_right = [0] * n
    parent_left = [None] * n
    parent_right = [None] * n

    # Base case: start on left[0]
    dp_left[0] = arr_l[0]
    dp_right[0] = 0

    for i in range(1, n):
        # Left side
        if dp_left[i-1] + arr_l[i] >= dp_right[i-1]:
            dp_left[i] = dp_left[i-1] + arr_l[i]
            parent_left[i] = ("L", i-1)  # came from left, picked rock
        else:
            dp_left[i] = dp_right[i-1]   # crossed, no rock picked
            parent_left[i] = ("R", i-1)

        # Right side
        if dp_right[i-1] + arr_r[i] >= dp_left[i-1]:
            dp_right[i] = dp_right[i-1] + arr_r[i]
            parent_right[i] = ("R", i-1)  # came from right, picked rock
        else:
            dp_right[i] = dp_left[i-1]    # crossed, no rock picked
            parent_right[i] = ("L", i-1)

    # Choose best ending
    if dp_left[-1] >= dp_right[-1]:
        max_sum = dp_left[-1]
        side, idx = "L", n-1
    else:
        max_sum = dp_right[-1]
        side, idx = "R", n-1

    # Backtrack path
    path = []
    while idx is not None:
        path.append((side, idx))
        if side == "L":
            parent = parent_left[idx]
        else:
            parent = parent_right[idx]
        if parent is None:
            break
        side, idx = parent

    path.reverse()
    return max_sum, path

def ferry_cars(L, cars):
    n = len(cars)
    sum = [0]*(n+1)
    for i in range(1, n+1):
        sum[i] = sum[i-1] + cars[i-1]

    memo = [set() for _ in range(n+1)]
    memo[0].add(0)

    max_cars = 0

    for i in range(n):
        for left_len in memo[i]:
            right_len = sum[i] - left_len

            if left_len + cars[i] <= L:
                memo[i+1].add(left_len + cars[i])
                max_cars = max(max_cars, i+1)
            
            if right_len + cars[i] <= L:
                memo[i+1].add(left_len)
                max_cars = max(max_cars, i+1)
    
    return max_cars

cars = [2, 2, 7, 4, 9, 8, 1, 7, 3, 3]
L = 20

def coin_game(coins):
    n = len(coins)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][i] = coins[i]

    for length in range(2, n+1):
        for i in range(n-length + 1):
            j = i + length - 1
            #we take the first coin
            option1 = coins[i] + min(
                dp[i+2][j] if i+2 <= j else 0,
                dp[i+1][j-1] if i+1 <= j-1 else 0)
            #we take the last coin
            option2 = coins[j] + min(
                dp[i+1][j-1] if i+1 <= j else 0,
                dp[i][j-2] if i <= j-1 else 0)

            dp[i][j] = max(option1, option2)
    return dp[0][n-1]

def longest_palindrome(sequence):
    n = len(sequence)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if i <= j:
                if sequence[i] == sequence[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

def longest_palindrome_string(string):
    n = len(string)
    max_string = 1

    for i in range(1, n):
        j = 1
        while i-j >= 0 and i+j <= n and string[i-j] == string[i+j]:
            max_string = max(max_string, 2j+1)
            j += 1
        j=0
        while i-j >= 0 and i+j <= n and string[i-j+1] == string[i+j]:
            max_string = max(max_string, 2j)
            j += 1
    return max_string


            
sequence = [2, 5, 3, 2, 3, 5, 6]

string = 'fcbabcg'
print(longest_palindrome_string(string))

coins = [6, 9, 1, 2, 16, 8]




   


    

money_grid = [
    [1, 0, 0, 0, 1],
    [0, 3, 2, 0, 1],
    [0, 0, 1, 0, 2],
    [0, 2, 1, 0, 0],
    [0, 0, 1, 0, 2]
]

grid = [
    [False, False, False, False],
    [True, False, False, False],
    [False, False, False, True],
    [False, False, False, False]
]

sequence = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

sum_sequence = [0,8,-4,-12,2,-10,-6,14,1,-9,5,13,-3,11,-7,15]

left_street = [0,8,4,12,2,10,6,14]
right_street = [1,9,5,13,3,11,7,15]


