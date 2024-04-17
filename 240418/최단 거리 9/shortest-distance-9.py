from heapq import heappop, heappush
V, E = map(int,input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    i,j,w = map(int,input().split())
    graph[i].append((j,w))
    graph[j].append((i,w))

start, end = map(int,input().split())
path = [-1]*(V+1)
INF = 10**9
dist = [INF]*(V+1)

def dijkstra(start):
    PQ = [(0, start)]
    dist[start] = 0

    while PQ:
        d, i = heappop(PQ)
        if dist[i] < d: continue

        for j,w in graph[i]:
            if dist[j] <= d+w: continue
            dist[j] = d+w
            heappush(PQ, (dist[j], j))
            path[j] = i
dijkstra(start)

j = end
ans = [end]
while j != start:
    j = path[j]
    ans.append(j)
print(dist[end])
print(*ans[::-1])