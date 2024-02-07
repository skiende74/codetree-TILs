N, K = map(int, input().split())
grid = [[0]*(N+1)] +[[0] + list(map(int, input().split())) for _ in range(N)]

#
prefix_sum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + grid[i][j]


ans = 0
# k = i+N+1-j
for i in range(1,N+1):
    for j in range(1,N+1):
        total = 0
        for i2 in range(max(0,i-K), min(i+K,N)+1):
            total += prefix_sum[i2][min(N, j+K-abs(i-i2))] - prefix_sum[i2][max(0, j-K+abs(i-i2)-1)]
        ans = max(ans, total)
print(ans)