def bottom_up_coins(C, capacity):
    #bottom up
    memo = [float('inf')]*(capacity+1)
    memo[0] = 0
    
    for i in range(1, capacity+1):
        suboptions = [(1 + memo[i-coin]) for coin in C if i-coin >= 0] 
        memo[i] = min(suboptions)
    return memo[capacity]



def top_down_coins(C, capacity, memo=None):

    if memo is None:
        memo = [None] * (capacity + 1)

    if capacity<0:
        return float('inf')
    if capacity == 0:
        return 0

    if memo[capacity] is not None:
        return memo[capacity]

    minimum_coins = float('inf')
    
    for coin in C:
        if capacity >= coin:
            current_minimum = 1 + top_down_coins(C, capacity-coin, memo)
            minimum_coins = min(minimum_coins, current_minimum)
    memo[capacity] = minimum_coins

    return memo[capacity]



coins = [1, 3, 4]
capacity = 6
print(top_down_coins(coins, capacity))
print(bottom_up_coins(coins, capacity))
            
