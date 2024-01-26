import sys 
from collections import deque

N, H, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def bfs(start):
    initialize(start)

    Q = deque([start])
    while Q:
        i,j = Q.popleft()

        dis, djs = [0,0,-1,1], [-1,1,0,0]

        for di, dj in zip(dis,djs):
            i2, j2 = i+di, j+dj

            if 0<=i2<N and 0<=j2<N and not visited[i2][j2] and grid[i2][j2] != 1:
                visited[i2][j2] = True
                dist[i2][j2] = min(dist[i2][j2], dist[i][j]+1)
                if grid[i2][j2] == 3:
                    return dist[i2][j2]
                Q.append((i2,j2))
    
    return -1

def initialize(start):
    global visited, dist
    MAX = sys.maxsize
    visited = [ [False]*N  for _ in range(N)]
    dist = [ [MAX]*N for _ in range(N) ]
    dist[start[0]][start[1]] = 0


answers = [ [0]*N for _ in range(N) ] 
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            answers[i][j] = bfs((i,j))


for i in range(N):
    for j in range(N):
        print(answers[i][j], end=' ')
    print()