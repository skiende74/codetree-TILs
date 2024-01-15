from copy import deepcopy

# 입력
N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(Q)]

# 바람
def wind2D(r1,c1,r2,c2):
    temp = grid[r1][c1]
    for i in range(r1, r2):
        grid[i][c1] = grid[i+1][c1]
    
    for j in range(c1, c2):
        grid[r2][j] = grid[r2][j+1]
    
    for i in range(r2, r1, -1):
        grid[i][c2] = grid[i-1][c2]
    
    for j in range(c2, c1, -1):
        grid[r1][j] = grid[r1][j-1]
    grid[r1][c1+1] = temp

def do_average(r1,c1,r2,c2):
    grid_old = deepcopy(grid)
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            total = 0
            count = 0
            for di, dj in zip([0,0,0,-1,1],[0,-1,1,0,0]):
                i2,j2= i+di, j+dj
                if 0<=i2<N and 0<=j2<M:
                    total += grid_old[i2][j2]
                    count += 1
            grid[i][j] = total//count
                              
    

# 본문
for r1,c1,r2,c2 in commands:
    r1,c1,r2,c2 = r1-1, c1-1, r2-1, c2-1
    wind2D(r1,c1,r2,c2)
    do_average(r1,c1,r2,c2)

for line in grid:
    print(' '.join(map(str, line)))