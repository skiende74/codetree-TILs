# 입력
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
r,c = map(int, input().split())

bomb_range = grid[r-1][c-1]


def in_bomb(i,j):
    return (i==r-1 or j==c-1) and abs(i-(r-1)) < bomb_range and abs(j-(c-1)) < bomb_range

for i in range(N):
    for j in range(N):
        if in_bomb(i,j):
            grid[i][j]=0

next_grid = [[0 for _ in range(N)] for _ in range(N)]
for j in range(N):
    next_row = N-1
    for i in range(N-1,-1,-1):
        if grid[i][j] != 0:
            next_grid[next_row][j] = grid[i][j]
            next_row -= 1

for i in range(N):
    print(' '.join(map(str, next_grid[i])))