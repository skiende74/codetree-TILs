# 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


# dfs
def dfs(i, j):

    dis, djs = [0,0,-1,1], [-1,1,0,0]

    for di, dj in zip(dis, djs):
        i2, j2 = i + di, j + dj

        if can_move(i2, j2):
            visited[i2][j2] = True

            dfs(i2, j2)

def can_move(i, j):
    in_range = 0<=i<N and 0<=j<M

    return in_range and not visited[i][j] and grid[i][j] > K # K : 수심

# 본문
safe_region_max = 0
K_max = 0
for K in range(1, 100+1):

    safe_region_count = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if can_move(i,j):
                visited[i][j]=True
                safe_region_count += 1
                dfs(i,j)

    if safe_region_count > safe_region_max:
        safe_region_max = safe_region_count
        K_max = K

print(f'{K_max} {safe_region_max}')