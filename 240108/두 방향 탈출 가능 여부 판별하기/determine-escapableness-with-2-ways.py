# 입력
N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

# dfs
result = False
visited = [[False]*M for _ in range(N)]
def dfs(i, j):
    global result

    dis, djs = [0,1],[1,0]

    for di,dj in zip(dis,djs):
        i2, j2 = i + di, j + dj

        if can_go(i2, j2):
            if (i2,j2) == (N-1, M-1):
                result = True
                return
            visited[i2][j2] = True
            dfs(i2,j2)

def can_go(i,j):
    in_range = 0<=i<N and 0<=j<M
    
    return in_range and not visited[i][j] and grid[i][j] == 1


dfs(0,0)
print('1' if result else '0')