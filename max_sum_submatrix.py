def max_sum_submatrix(M):
    m = len(M)
    dp = [[0]*m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            dp[i][j] = M[i][j]
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            if i > 0 and j > 0:
                dp[i][j] -= dp[i-1][j-1]
    
    max_sum = float('-inf')
    #calculate sums of every possible sub matrix
    for i in range(m):
        for k in range(m):
            for j in range(m):
                for l in range(m):
                    current_sum = dp[k][l] 
                    if i > 0:
                        current_sum -= dp[i-1][l] 
                    if j > 0:
                        current_sum -= dp[j-1][k] 
                    if i > 0 and j > 0:
                        current_sum += dp[i-1][j-1]
                    #update the memo if the current sub matrix is larger than the current max 
                    max_sum = max(current_sum, max_sum)
    
    return max_sum
              