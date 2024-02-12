from math import sqrt

N, M = map(int, input().split())
pose = [list(map(int, input().split())) for _ in range(N)]
selected = []

ans = 10**9
def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def calc():
    K = len(selected)
    result = 0
    for i in range(K):
        for j in range(i+1, K):
            result = max(result, dist(pose[selected[i]], pose[selected[j]]))
    return result

def dfs(i, n):
    global ans

    if n == M:
        ans = min(ans, calc())
        return
    if i == N: return

    dfs(i+1, n)
    
    selected.append(i)
    dfs(i+1, n+1)
    selected.pop()
dfs(0, 0)
print(ans)