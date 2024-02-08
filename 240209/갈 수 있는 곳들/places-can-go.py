from collections import deque
N, K = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

Q = deque()
for _ in range(K):
    r, c = map(int,input().split())
    i, j = r-1, c-1
    Q.append((i,j))

def bfs():
    count = 0
    while Q:
        i, j = Q.popleft()

        dis, djs = [0,0,-1,1], [-1,1,0,0]
        for di, dj in zip(dis,djs):
            i2, j2 = i+di, j+dj
            if 0<=i2<N and 0<=j2<N and not visited[i2][j2] and grid[i2][j2] == 0:
                visited[i2][j2] = True
                count += 1
                Q.append((i2,j2))
    return count

visited = [[False]*(N) for _ in range(N)]
print(bfs())