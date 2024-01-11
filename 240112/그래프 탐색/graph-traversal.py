import sys

# 입력
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j) # 인접리스트
    graph[j].append(i)

# dfs
def dfs(i):
    global count
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            count += 1
            dfs(j)

# 본문
visited = [False]*(N+1)
visited[1] = True
count = 0
dfs(1)
print(count)