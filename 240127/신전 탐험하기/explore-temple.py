N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

dp[0] = grid[0].copy()
for i in range(1, N):
    for j in range(3):
        dp[i][j] = max(dp[i][j], *dp[i-1][:j], *dp[i-1][j+1:]) + grid[i][j]

print(max(dp[-1]))