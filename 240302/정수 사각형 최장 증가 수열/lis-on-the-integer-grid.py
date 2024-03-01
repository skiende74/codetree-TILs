N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
dp = [[1]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dis, djs = [0,0,-1,1], [-1,1,0,0]
        for di, dj in zip(dis,djs):
            i2, j2 = i+di, j+dj
            if not(0<=i2<N and 0<=j2<N): continue
            if grid[i][j] > grid[i2][j2]:
                dp[i][j] = max(dp[i][j], dp[i2][j2]+1)
            if grid[i][j] < grid[i2][j2]:
                dp[i2][j2] = max(dp[i2][j2], dp[i][j]+1)
print(max(map(max, *dp)))