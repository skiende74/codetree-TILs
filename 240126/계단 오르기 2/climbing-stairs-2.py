N = int(input())
coins = [0] + list(map(int, input().split()))

K = 4

dp = [[0]*(K) for _ in range(N+1)]
# dp[i][k]

for k in range(K):
    for i in range(1, N+1):
        # 두칸씩
        if i>=2:
            dp[i][k] = max(dp[i][k], dp[i-2][k] + coins[i])
        # 한칸씩
        if k>=1:
            dp[i][k] = max(dp[i][k], dp[i-1][k-1] + coins[i])
    
print(max(dp[-1]))