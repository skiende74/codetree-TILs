N, M = map(int, input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [False]*(N+1)
visited[1] = True
def dfs(a):
    global count
    for v in graph[a]:
        if not visited[v]:
            visited[v] = True
            count = count + 1
            dfs(v)

dfs(1)
print(count)