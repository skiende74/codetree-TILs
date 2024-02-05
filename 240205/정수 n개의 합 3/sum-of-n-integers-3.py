N, K = map(int, input().split())
grid = [[0]*(N+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]

prefix_sum = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1,N+1):
        prefix_sum[i][j] = -prefix_sum[i-1][j-1] + prefix_sum[i][j-1] + \
         prefix_sum[i-1][j] + grid[i][j]

ans = 0
for i in range(K, N+1):
    for j in range(K, N+1):
        value = prefix_sum[i][j] - prefix_sum[i-K][j] - \
        prefix_sum[i][j-K] + prefix_sum[i-K][j-K]
        ans = max(ans, value)
print(ans)