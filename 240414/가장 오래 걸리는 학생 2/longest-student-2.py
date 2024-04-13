from heapq import heappop, heappush

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    i,j,w = map(int,input().split())
    graph[j].append((i, w))

PQ = [(0, V)]

dist = [10**9]*(V+1)

dist[V] = 0
while PQ:
    d, i = heappop(PQ)

    for j, w in graph[i]:
        if dist[j] > dist[i]+d:
            dist[j] = dist[i]+d
            heappush(PQ, (dist[j], j))

print(max(dist[1:]))