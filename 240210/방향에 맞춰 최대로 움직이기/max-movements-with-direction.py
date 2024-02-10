N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
grid_dir = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]


dir2vec = [0,(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def dfs(i, j):
    global max_move, move

    d = dir2vec[grid_dir[i][j]]
    for k in range(1, N):
        i2, j2 = i+d[0]*k, j+d[1]*k
        if 0<=i2<N and 0<=j2<N and grid[i2][j2] > grid[i][j]:
            move += 1
            max_move = max(max_move, move)
            dfs(i2, j2)
            move -= 1

r,c = map(int,input().split())
move, max_move = 0,0
dfs(r-1,c-1)

print(max_move)