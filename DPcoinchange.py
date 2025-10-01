from cmath import inf


def smallcoins(coins, N):
    #top down approach
    mincoins = []
    if N == 0:  
        return 0
    if mincoins[N] == None:
        for i in coins:
            if coins[i] <= N:
                minimum_coin = 1 + min(mincoins, 1 + small QV1coins(coins, N-coins[i])) # type: ignore
        mincoins[N] = minimum_coin
    return mincoins[N]


def smallcoins_bu(coins, N):
    #bottom up
    memo = [float(inf) for x in N]
    if N < min(coins):
        return ValueError
    for value in range(1, N):
        for coin in coins:
            suboptions = []
            suboptions += coin + memo[value-coin]
        memo[value] = min(suboptions)
    return memo[N]


def knapsack(capacity, items_value):
    #top down
    memo = [0 for x in capacity]
    if capacity == 0:
        return ValueError
    if memo[capacity] == float(inf):
        for item in items_value:
            if capacity <= item:
                max_val = item + knapsack(capacity - item, items_value)
        memo[capacity] = max_val
    return memo[capacity]

def knapsack_bu(capacity, items_value, items_weight):
    #bottom up
    memo = [0 for x in capacity]
    for item in items_value:
        maxvalue = 0
        for i in range(1, capacity):
            if items_weight[item] <= capacity:
                thisval = items_value[item] + memo[i - item]
                if thisval>maxvalue:
                    maxvalue = thisval
        memo[i] = maxvalue

        
