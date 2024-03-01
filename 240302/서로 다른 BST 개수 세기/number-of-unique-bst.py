N = int(input())
dp = [[-1,-1],[1,0]]+[[-1,-1] for _ in range(N-1)]
for i in range(2,N+1):
    dp[i][0] = dp[i-1][0]*2 + dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]*3
print(dp[N][0])