V, E = map(int,input().split())
s1,s2, e = map(int,input().split())

INF = 10**9
grid = [[INF]*(V+1) for _ in range(V+1)]
for i in range(1,V+1): grid[i][i]=0
for _ in range(E):
    i,j,w = map(int,input().split())
    grid[i][j] = w
    grid[j][i] = w

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])

#print(*grid,sep='\n')
ans = INF
for i in range(1,V+1):
    ans=min(ans,grid[s1][i]+grid[s2][i]+grid[i][e])
print(ans if ans!=INF else -1)