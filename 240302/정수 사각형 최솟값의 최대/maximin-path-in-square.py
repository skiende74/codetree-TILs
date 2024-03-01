N = int(input())
MAX = 1_000_000 + 1
grid = [list(map(int,input().split())) for _ in range(N)]
dp = [[MAX]*N for _ in range(N)]
m = grid[0][0]
for i in range(N):
    m = min(m, grid[i][0])
    dp[i][0] = m

m = grid[0][0]
for j in range(N):
    m = min(m, grid[0][j])
    dp[0][j] = m

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = min(max(dp[i][j-1], dp[i-1][j]), grid[i][j])
print(dp[-1][-1])