N,M = map(int,input().split())
edges = [ list(map(int,input().split())) for _ in range(M)]

import sys
graph = [ [1000_000_000]*(N) for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for i,j,d in edges:
    i,j = i-1,j-1
    graph[i][j] = min(graph[i][j], d)

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

floyd()
for i in range(N):
    print(' '.join(map(str, graph[i])))