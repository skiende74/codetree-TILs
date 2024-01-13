from collections import deque
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10000)
# 입력
N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())

# bfs
def dfs(i,j):
    global visited, heap

    dis, djs = [0,0,-1,1], [-1,1,0,0]
    for di,dj in zip(dis, djs):
        i2,j2 = i+di, j+dj
        if can_move(i2, j2):
            visited[i2][j2] = True
            heappush(heap, (-grid[i2][j2],(i2, j2)))
            dfs(i2,j2)
    
    return heap[0] if heap else []

def can_move(i,j):
    global visited, r,c
    in_range = 0<=i<N and 0<=j<N

    return in_range and not visited[i][j] and grid[i][j] < grid[r][c]

# 본문
r-=1
c-=1
for _ in range(K):
    visited = [[False]*N for _ in range(N)]
    visited[r][c] = True
    heap = []

    heap = dfs(r,c)
    if heap:
        (_,(r,c)) = heap
        #print(f'{r+1} {c+1}')
    else:
        break

print(f'{r+1} {c+1}')