N = int(input())
seq = [0] + list(map(int,input().split()))
INF = 10**9
dp = [INF]*(N+1)
dp[1] = 0
for i in range(2, N+1):
    for j in range(1, i):
        if j+seq[j] >= i:
            dp[i] = min(dp[i], dp[j]+1)
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])