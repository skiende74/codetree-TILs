import sys
sys.setrecursionlimit(2501)

# 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# dfs
def dfs(i,j):
    dis, djs = [0,0,-1,1], [-1,1,0,0]
    for di, dj in zip(dis, djs):
        i2,j2 = i+di, j+dj

        if 0<=i2<N and 0<=j2<M and not visited[i2][j2] and grid[i2][j2]>K:
            visited[i2][j2] = True
            dfs(i2,j2)

result = [-1]*101
for K in range(1,101):
    count = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j]>K:
                count += 1
                visited[i][j] = True
                dfs(i,j)
    result[K] = count

for i in range(1,101):
    if max(result) == result[i]:
        print(f'{i} {result[i]}')
        break