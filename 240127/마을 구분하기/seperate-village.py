# 입력
N = int(input())
grid = [ list(map(int, input().split())) for _ in range(N)]

# dfs
def dfs(i, j):
    global in_count
    dis, djs = [0,0,-1,1], [-1,1,0,0]
    for di, dj in zip(dis, djs):
        i2, j2 = i+di, j+dj
        if 0<=i2<N and 0<=j2<N and not visited[i2][j2] and grid[i2][j2] == 1:
            visited[i2][j2] = True
            in_count += 1
            dfs(i2,j2)

visited = [ [False]*N for _ in range(N)]
count = 0
result = []
for i in range(N):
    for j in range(N):
        in_count = 1
        if not visited[i][j] and grid[i][j] == 1:
            visited[i][j]=True
            dfs(i,j)
            count += 1
            result.append(in_count)

result.sort()
print(count)
for w in result:
    print(w)