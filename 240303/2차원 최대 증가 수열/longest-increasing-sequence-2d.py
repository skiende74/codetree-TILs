import sys
INT_MIN = -sys.maxsize
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[INT_MIN]*M for _ in range(N)]
dp[0][0] = 1

def max2d(A):
    return max(map(max, A))

for i1 in range(N):
    for j1 in range(N):
        for i2 in range(i1):
            for j2 in range(j1):
                if grid[i2][j2] < grid[i1][j1] and dp[i2][j2] != INT_MIN:
                    dp[i1][j1] = max(dp[i1][j1], dp[i2][j2]+1)

print(max2d(dp))