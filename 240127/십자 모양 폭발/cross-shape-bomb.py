# 입력
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
r,c = map(int, input().split())

num = grid[r-1][c-1]

i,j = r-1,c-1
for k in range(num):
    dis,djs = [0,0,-1,1],[-1,1,0,0]
    for di,dj in zip(dis,djs):
        i2,j2 = i+k*di, j+k*dj
        if 0<=i2<N and 0<=j2<N:
            grid[i2][j2] = 0

next_grid = [[0 for _ in range(N)] for _ in range(N)]
for j in range(N):
    next_row = N-1
    for i in range(N-1,-1,-1):
        if grid[i][j] != 0:
            next_grid[next_row][j] = grid[i][j]
            next_row -= 1

for i in range(N):
    print(' '.join(map(str, next_grid[i])))