N = int(input())
points = [(0,0)] + [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N+1)]

for i in range(N+1):
    for j in range(i+1, N+1):
        if i != j:
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                graph[i].append(j)
                graph[j].append(i)

def dfs(i):
    global answer
    if len(result) == N+2 and result[-1] == start:
        answer += 1
        return
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            result.append(j)
            dfs(j)
            result.pop()
            visited[j] = False

answer = 0
start = 0
result = [0]
visited = [False]*(N+1)
dfs(start)
print(answer)