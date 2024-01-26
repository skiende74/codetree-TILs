N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N)]
# [N개 층][1층방순서][현재층방순서] 순

dp[0][0][0] = grid[0][0]
dp[0][1][1] = grid[0][1]
dp[0][2][2] = grid[0][2]
for l in range(3): # 1층 방번호
    for i in range(1, N):
        for j in range(3): #현재방번호
            for k in range(3): #직전방번호
                if (i<N-1 and j!=k) or (i==N-1 and j!=k and j!=l):
                    dp[i][l][j] = max(dp[i][l][j], dp[i-1][l][k] + grid[i][j])

maxVal = -1

for i in range(3):
    for j in range(3):
        maxVal = max(maxVal, dp[N-1][i][j])

print(maxVal)