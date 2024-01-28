from copy import deepcopy

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

N_BOMB = 0
bombs_pose = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            N_BOMB += 1

bombs = []
def dfs(num):
    if num == N_BOMB:
        count_region()
        return
    
    for i in range(3):
        bombs.append(i)
        dfs(num+1)
        bombs.pop()

dis = [[-2,-1,1,2],[-1,0,0,1],[-1,-1,1,1]]
djs = [[0]*4, [0,-1,1,0],[-1,1,-1,1]]

def count_region():
    global result, new_grid
    bomb_idx = 0
    new_grid = deepcopy(grid)

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                b = bombs[bomb_idx]
                for di,dj in zip(dis[b],djs[b]):
                    i2,j2 = i+di, j+dj
                    if 0<=i2<N and 0<=j2<N:
                        new_grid[i2][j2] = 1
                bomb_idx+=1
    
    total = 0
    for i in range(N):
        total += sum(new_grid[i])
    result = max(result, total)

result=-1
dfs(0)

print(result)