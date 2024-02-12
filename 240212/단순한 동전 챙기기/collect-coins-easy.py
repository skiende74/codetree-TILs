N = int(input())
M = 9
grid = [list(input()) for _ in range(N)]
pose = [None] + [None]*9
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'E':
            end = (i,j)
        elif grid[i][j] != '.':
            pose[int(grid[i][j])] = (i,j)

INF = 10**9
count, ans = 0, INF

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def dfs(i, j, chosen):
    global ans, count

    if i == 9+1:
        return
    if j == 3:
        ans = min(ans, count + dist(chosen, end))
        return
    
    dfs(i+1, j, chosen)

    if pose[j+1]:
        count += dist(chosen, pose[j+1])
        dfs(i+1, j+1, pose[j+1])
        count -= dist(chosen, pose[j+1])

dfs(1, 0, start)
if ans == INF:
    print(-1)
else:
    print(ans)