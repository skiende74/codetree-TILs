from collections import defaultdict
from copy import deepcopy

N,M,r,c = map(int, input().split())
r,c = r-1, c-1
grid = [[False]*N for _ in range(N)]
grid[r][c] = True

for t in range(M):
    new_grid = deepcopy(grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                dis,djs = [-1,1,0,0],[0,0,-1,1]
                for di,dj in zip(dis,djs):
                    k = 2**t
                    i2,j2= i+k*di, j+k*dj

                    if 0<=i2<N and 0<=j2<N:
                        new_grid[i2][j2] = True
    
    grid = new_grid

total = 0
for i in range(N):
    total += sum(grid[i])
print(total)