V, E = map(int,input().split())
grid = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    i, j = map(int,input().split())
    grid[i][j] = 1
for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if grid[i][k] and grid[k][j]:
                grid[i][j] = 1

for i in range(1,V+1):
    total = 0
    for j in range(1,V+1):
        total += 0 if grid[i][j] or grid[j][i] else 1
    print(total-1)