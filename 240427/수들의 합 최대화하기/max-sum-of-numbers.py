import sys
sys.setrecursionlimit(2*10**5)

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
visited = set()

max_val = -1
def dfs(i):
    global max_val
    if len(answers)==N:
        max_val = max(max_val, sum(answers))
        return
    for j in range(N):
        if j in visited: continue
        visited.add(j)
        answers.append(grid[i][j])
        dfs(i+1)
        answers.pop()
        visited.remove(j)

answers= []
dfs(0)
print(max_val)