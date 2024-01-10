from collections import deque
import sys

sys.setrecursionlimit(10000)
# 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# bfs
def bfs(start):
    q = deque([start])
    while q:
        v = q.popleft()

# dfs
visited = [[False]*N for _ in range(N)]
escape = 0
def dfs(i,j):
    global escape
    dis, djs = [0,0,-1,1],[-1,1,0,0]

    for di,dj in zip(dis, djs):
        i2,j2 = i+di, j+dj

        if 0<=i2<N and 0<=j2<N and not visited[i2][j2] and grid[i2][j2]:
            visited[i2][j2] = True
            if (i2, j2) == (N-1, M-1):
                escape = 1
                return
            dfs(i2,j2)



# 본문
dfs(0,0)
visited[0][0] = True
print(escape)