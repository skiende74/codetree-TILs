# 입력
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# dfs
visited = [[False for _ in range(N)] for _ in range(N)]
def dfs(i, j):
    global in_count
    dis, djs = [0,0,-1,1], [-1,1,0,0]
    for di, dj in zip(dis, djs):
        i2, j2 = i+di, j+dj
        if 0<=i2<N and 0<=j2<N and not visited[i2][j2] and grid[i2][j2] == 1:
            visited[i2][j2] = True
            in_count += 1
            dfs(i2, j2)

# 본문
result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j]==1:
            in_count = 1
            visited[i][j] = True
            dfs(i, j)
            result.append(in_count)

result.sort()
print(len(result))
for r in result:
    print(r)