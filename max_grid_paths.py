def max_paths_grid(Grid):
    n = len(Grid)
    if n == 0:
        return 0
    
    dp = [[0] * n for _ in range(n)]

    if Grid[0][n-1] == 0:
        return 0
    dp[0][n-1] = 1


    for i in range(n):
        for j in range(n-1, -1, -1):
            if Grid[i][j] == 0:
                dp[i][j] = 0
                continue

            if i-1 >= 0:
                dp[i][j] += dp[i-1][j]
            
            if j+1 < n:
                dp[i][j] += dp[i][j+1]
    
    return dp[n-1][0]


def max_money_grid(Grid):
    n = len(Grid)
    if n == 0:
        return 0
    
    dp = [[0] * n for _ in range(n)]

    if Grid[0][n-1] == 0:
        return 0
    dp[0][n-1] = 1


    for i in range(n):
        for j in range(n-1, -1, -1):
            if Grid[i][j] == 0:
                dp[i][j] = 0
                continue

            if j == n:
                dp[i][j] = dp[i-1][j]
            
            elif i == 0:
                dp[i][j] = dp[i][j+1]
            
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j+1]) + Grid[i][j]

    
    return dp[n-1][0]