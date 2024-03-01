N = int(input())
MAX = 1_000_000 + 1
grid = [list(map(int,input().split())) for _ in range(N)]
dp = [[MAX]*N for _ in range(N)]

def initialize():
    dp[0][0] = grid[0][0]
    for i in range(N):
        dp[i][0] = min(dp[i-1][0], grid[i][0])

    for j in range(N):
        dp[0][j] = min(dp[0][j-1], grid[0][j])

initialize()
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = min(max(dp[i][j-1], dp[i-1][j]), grid[i][j])
print(dp[-1][-1])