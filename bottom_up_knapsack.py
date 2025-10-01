from array import array


def bottom_up_knapsack(items: array, capacity):
    memo = [None]*(capacity+1)
    memo[0] = 0

    for i in range(1, capacity+1):
        for item in items:
            weight = item[0]
            value = item[1]
            memo[i] = max(memo[i], value + memo[i - weight])
    return memo[capacity]
