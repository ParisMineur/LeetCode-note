## template for dynamic programming

## define state
dp = [][]

## initialize state
dp[0][0] = x
dp[0][1] = y

## state transform
for i in range(n):
    for j in range(m):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1])  ## for example
        
return dp[m][n]
