from collections import deque
N, K = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*(N) for _ in range(N)]

count = 0
Q = deque()
for _ in range(K):
    r, c = map(int,input().split())
    i, j = r-1, c-1
    count += 1
    visited[i][j] = True
    Q.append((i,j))

def bfs():
    global count
    while Q:
        i, j = Q.popleft()

        dis, djs = [0,0,-1,1], [-1,1,0,0]
        for di, dj in zip(dis,djs):
            i2, j2 = i+di, j+dj
            if 0<=i2<N and 0<=j2<N and not visited[i2][j2] and grid[i2][j2] == 0:
                visited[i2][j2] = True
                count += 1
                Q.append((i2,j2))


print(bfs())