# 입력
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    A[i].append(j)
    A[j].append(i)

# dfs
def dfs(i):
    for j in A[i]:
        if not visited[j]:
            visited[j] = True
            dfs(j)


# 본문
visited = [False]*(N+1)
count = 0
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = True
        count += 1
        dfs(i)
print(count)