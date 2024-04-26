V = int(input())
grid = [list(map(int,input().split())) for _ in range(V)]
for i in range(V): grid[i][i]=1

for i in range(V):
    for j in range(V):
        for k in range(V):
            if grid[i][k] and grid[k][j]:
                grid[i][j] = 1
for g in grid:
    print(*g)