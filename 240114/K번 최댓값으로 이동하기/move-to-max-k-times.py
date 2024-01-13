from collections import deque
from heapq import heappush, heappop

# 입력
N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())

# bfs
visited = []
def bfs(i0,j0):
    global visited
    q = deque([(i0,j0)])
    heap = []

    visited = [[False]*N for _ in range(N)]
    visited[i0][j0] = True
    while q:
        i, j = q.popleft()
        dis, djs = [0,0,-1,1], [-1,1,0,0]
        for di,dj in zip(dis, djs):
            i2,j2 = i+di, j+dj
            if can_move(i2, j2, i0,j0):
                visited[i2][j2] = True
                heappush(heap, (-grid[i2][j2],(i2, j2)))
                q.append((i2,j2))
    
    return heap[0] if heap else []

def can_move(i,j, i0, j0):
    global visited
    in_range = 0<=i<N and 0<=j<N

    return in_range and not visited[i][j] and grid[i][j] < grid[i0][j0]

# 본문
r-=1
c-=1
for _ in range(K):
    heap = bfs(r,c)
    if heap:
        (_,(r,c)) = heap
        #print(f'{r+1} {c+1}')
    else:
        break

print(f'{r+1} {c+1}')