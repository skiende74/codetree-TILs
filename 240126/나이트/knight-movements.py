from collections import deque
import sys

N = int(input())
r1,c1, r2, c2 = map(int, input().split())
MAX = sys.maxsize

visited = [ [False]*N for _ in range(N)]
dist = [ [MAX]*N for _ in range(N)]
dist[r1-1][c1-1] = 0

def bfs(start):
    Q = deque([start])

    while Q:
        i, j = Q.popleft()

        dis, djs = [1,1,2,2,-1,-1,-2,-2], [-2,2,-1,1,-2,2,-1,1]

        for di, dj in zip(dis,djs):
            i2, j2 = i+di, j+dj

            if 0<=i2<N and 0<=j2<N and not visited[i2][j2]:
                visited[i2][j2] = True
                dist[i2][j2] = min(dist[i2][j2], dist[i][j]+1)
                Q.append((i2,j2))

bfs((r1-1,c1-1))
print(dist[r2-1][c2-1])