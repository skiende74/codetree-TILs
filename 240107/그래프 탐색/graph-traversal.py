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
count = 0
def dfs(i):
    global count
    for j in A[i]:
        if not visited[j]:
            visited[j] = True
            count += 1
            dfs(j)


# 본문
visited = [False]*(N+1)
visited[1] = True
dfs(1)
print(count)