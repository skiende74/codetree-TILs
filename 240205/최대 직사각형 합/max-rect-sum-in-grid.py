N = int(input())
grid = [[0]*(N+1)] + [[0] + list(map(int,input().split())) for _ in range(N) ]

prefix_sum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        prefix_sum[i][j] = -prefix_sum[i-1][j-1] + prefix_sum[i][j-1] + \
        prefix_sum[i-1][j] + grid[i][j]

ans = -1000_000_000
dp = [0]*(N+1)
for i1 in range(1,N+1):
    for i2 in range(i1, N+1):
        dp = [-1000_000_000]*(N+1)
        for j in range(1, N+1):
            now = prefix_sum[i2][j] -\
            prefix_sum[i2][j-1] - prefix_sum[i1-1][j] + prefix_sum[i1-1][j-1]

            dp[j] = max(dp[j-1]+now, now)
        ans = max(ans, max(dp))

print(ans)