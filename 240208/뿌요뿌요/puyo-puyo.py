# 입력
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# dfs
visited=[[False]*N for _ in range(N)]
def dfs(i,j):
    global block_size

    dis, djs = [0,0,-1,1],[-1,1,0,0]
    for di, dj in zip(dis, djs):
        i2, j2= i + di, j + dj
        if can_move(i2, j2) and grid[i2][j2] == grid[i][j]:
            visited[i2][j2] = True
            block_size += 1
            dfs(i2, j2)

def can_move(i,j):
    in_range = 0<=i<N and 0<=j<N

    return in_range and not visited[i][j]


# 본문

explosion_count = 0
block_size_max = 0

for i in range(N):
    for j in range(N):
        if can_move(i,j):
            visited[i][j] = True
            block_size = 1
            dfs(i,j)

            if block_size >= 4:
                explosion_count += 1
            block_size_max = max(block_size_max, block_size)

print(f'{explosion_count} {block_size_max}')