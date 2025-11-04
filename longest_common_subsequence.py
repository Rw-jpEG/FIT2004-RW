from array import array


def longest_common_subsequence(a: array, b: array):
    n = len(a)
    m = len(b)
    dp = [[] * m for _ in range(n)]

    dp[0][0] = 0

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]