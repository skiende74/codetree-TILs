from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
S = int(input())
INF = 10**9
graph = defaultdict(lambda: defaultdict(lambda:INF))

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u][v] = w
    graph[v][u] = w

dist = [INF]*(V+1)
dist[S] = 0

Q = [(0,S)]
while Q:
    _, i = heappop(Q)
    for j,w in graph[i].items():
        if dist[j] > dist[i]+w:
            dist[j] = dist[i]+w
            heappush(Q, (dist[j], j))
for d in dist[1:]:
    print(d if d!=INF else -1)