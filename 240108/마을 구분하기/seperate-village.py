# 입력
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# dfs
visited = [[False]*N for _ in range(N)]
def dfs(i,j):
    global count
    dis, djs = [0,0,-1,1],[-1,1,0,0]
    for di, dj in zip(dis, djs):
        i2, j2 = i + di, j + dj

        if can_move(i2, j2):
            visited[i2][j2] = True
            count += 1
            dfs(i2,j2)

def can_move(i,j):
    in_range = 0<=i<N and 0<=j<N

    return in_range and not visited[i][j] and grid[i][j] == 1

# 본문

village_count = 0
counts = []
for i in range(N):
    for j in range(N):
        if can_move(i,j):
            visited[i][j] = True
            count = 1
            village_count += 1
            dfs(i,j)
            counts.append(count)

print(village_count)
print('\n'.join(map(str, sorted(counts))))