# 입력
N, M = map(int, input().split())
grid = [ list(map(int,input().split())) for _ in range(N)]

# dfs
def dfs(i,j):
    dis, djs = [1,0], [0,1]
    for di, dj in zip(dis, djs):
        i2, j2 = i+di, j+dj
        if 0<=i2<N and 0<=j2<M and grid[i2][j2] == 1 and not visited[i2][j2]:
            visited[i2][j2] = True
            dfs(i2, j2)

# 본문
visited = [[False]*M for _ in range(N)]
visited[0][0] = True
dfs(0,0)

if visited[-1][-1]:
    print(1)
else:
    print(0)