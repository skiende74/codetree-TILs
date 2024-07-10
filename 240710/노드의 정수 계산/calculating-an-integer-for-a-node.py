import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline
def dfs(i):
    if dp[i] != INF: return dp[i]
    dp[i] = sum([dfs(j) for j in graph[i]]) + seq[i]
    return dp[i]

N = int(input())

graph = [ [] for _ in range(N+1)]
seq = [0]*(N+1)
INF = 10**9
for i in range(2, N+1):
    t, a, p = map(int, input().split())
    graph[p].append(i)
    seq[i] = a
    if t == 0: seq[i] *= -1

dp = [INF]*(N+1)
print(dfs(1))