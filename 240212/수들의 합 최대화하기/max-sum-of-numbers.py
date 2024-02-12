N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [False]*N
selected = []
ans = 0
def dfs_perm():
    global ans
    if len(selected) == N:
        ans = max(ans, sum(selected))
        return

    for j in range(N):
        if visited[j]: continue
        visited[j] = True
        selected.append(grid[len(selected)][j])
        dfs_perm()
        visited[j] = False
        selected.pop()

dfs_perm()
print(ans)