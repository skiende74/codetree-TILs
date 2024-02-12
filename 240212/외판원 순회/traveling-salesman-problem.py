N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
selected = []
ans = 10**9
def dfs_perm(i):
    global ans

    if len(selected) == N-1:
        if grid[i][0] != 0:
            ans = min(ans, sum(selected)+grid[i][0])
        return
    
    for j in range(1, N):
        if visited[j]: continue
        if grid[i][j] == 0: continue

        visited[j] = True
        selected.append(grid[i][j])
        dfs_perm(j)
        visited[j] = False
        selected.pop()
    
dfs_perm(0)
print(ans)