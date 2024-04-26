N = int(input())
grid = [[0]*(N+1)]+[[0]+list(map(int,input().split())) for _ in range(N)]

answer = 0
max_val = 10**9
def dfs(i):
    global max_val, answer, cnt
    if cnt == N:
        if i==1: max_val = min(max_val, answer)
        return
    for j in range(1,N+1):
        if visited[j]: continue
        if grid[i][j] == 0: continue
        visited[j] = True
        answer += grid[i][j]
        cnt += 1
        dfs(j)
        cnt -= 1
        answer -= grid[i][j]
        visited[j] = False
cnt = 0
visited = [False]*(N+1)
dfs(1)
print(max_val)