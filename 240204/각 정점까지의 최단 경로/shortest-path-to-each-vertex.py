from heapq import heappush, heappop

readlist = lambda:list(map(int,input().split()))
N, M = readlist()
k = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i,j,d = readlist()
    graph[i].append((j, d))
    graph[j].append((i, d))

import sys
MAX=sys.maxsize
dist = [MAX]*(N+1)
def dijkstra(start):
    pq = [(0,start)]
    dist[start] = 0
    while pq:
        d, i = heappop(pq)

        for i2, d2 in graph[i]:
            if d + d2 < dist[i2]:
                dist[i2] = d+d2
                heappush(pq, (dist[i2], i2))

dijkstra(k)
dist = list(map(lambda x: str(x) if x<MAX else '-1', dist))
print('\n'.join(dist[1:]))