# 입력
N, M = map(int, input().split())
coins = list(map(int, input().split()))

dp = [[0]*(M+1) for _ in range(M+1)]
for i in range(1, M+1):
    for c in coins:
        if i-c>=0:
            dp[i][i] = max(dp[i][i], dp[i-c][i-c]+1)

if dp[M][M]==0:
    dp[M][M]=-1

print(dp[M][M])