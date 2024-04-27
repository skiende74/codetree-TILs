V, E = map(int,input().split())
INF = 10**9
grid = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    i,j,w = map(int,input().split())
    grid[i][j] = w



for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

print(min([ grid[i][i] for i in range(1,V+1)]))