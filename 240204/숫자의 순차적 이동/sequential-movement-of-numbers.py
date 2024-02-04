from copy import deepcopy
N, M = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

pose = {}
for i in range(N):
    for j in range(N):
        pose[grid[i][j]] = (i,j)

for _ in range(M):
    #new_pose = deepcopy(pose)
    for k in range(1,N*N+1):
        num, (i,j) = k, pose[k]
        dis,djs = [-1,1,0,0],[0,0,-1,1]
        priority = -1
        for di in range(-1,2):
            for dj in range(-1, 2):
                if (di,dj) == (0,0):
                    continue
                i2,j2 = i+di, j+dj
                if 0<=i2<N and 0<=j2<N and grid[i2][j2]>priority:
                    i_next, j_next = i2, j2
                    priority = grid[i2][j2]
        
        grid[i_next][j_next], grid[i][j] = grid[i][j], grid[i_next][j_next]
        pose[grid[i_next][j_next]], pose[grid[i][j]] = pose[grid[i][j]], pose[grid[i_next][j_next]]
for i in range(N):
    for j in range(N):
        print(grid[i][j], end=' ')
    print()