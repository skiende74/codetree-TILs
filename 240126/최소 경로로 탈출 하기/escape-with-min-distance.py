from collections import deque
import sys

# 입력
N, M = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(N)]
dist = [ [sys.maxsize]*M for _ in range(N) ]
dist[0][0] = 0
visited = [ [False]*M for _ in range(N)]

# BFS
def bfs(start):
    Q = deque([start])
    while Q:
        i,j = Q.popleft()

        dis, djs = [0,0,-1,1], [-1,1,0,0]

        for di, dj in zip(dis, djs):
            i2, j2 = i+di, j+dj

            if 0<=i2<N and 0<=j2<M and not visited[i2][j2] and grid[i2][j2] == 1:
                visited[i2][j2] = True
                dist[i2][j2] = min(dist[i2][j2], dist[i][j]+1)
                Q.append((i2, j2))

bfs((0,0))
print(dist[N-1][M-1])