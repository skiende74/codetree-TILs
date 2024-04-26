V,M = map(int,input().split())
INF = 10**9
grid = [[INF]*(V+1)]+[[INF]+list(map(int,input().split())) for _ in range(V)]

for k in range(1,V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])

for _ in range(M):
    i,j = map(int, input().split())
    print(grid[i][j])