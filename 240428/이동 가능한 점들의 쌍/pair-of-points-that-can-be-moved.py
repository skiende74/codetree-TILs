V, E, P, Q = map(int,input().split())

INF = 10**9
grid=[[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    i,j,w = map(int,input().split())
    grid[i][j] = w

for i in range(1, V+1):
    grid[i][i] = 0
for k in range(1,V+1):
    for i in range(1,V+1):  
        for j in range(1,V+1):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])
ans = 0
count_ = 0
for _ in range(Q):
    i, j = map(int,input().split())
    
    dist = INF
    for a in range(1,P+1):
        dist = min(dist, grid[i][a]+grid[a][j])
    if dist >= INF: continue

    ans += dist
    count_ += 1
        
print(count_)
print(ans)