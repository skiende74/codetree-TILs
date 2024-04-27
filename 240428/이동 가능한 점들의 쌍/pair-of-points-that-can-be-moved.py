V, E, P, Q = map(int,input().split())

INF = 10**9
grid=[[INF]*(V+1) for _ in range(V+1)]
red_pass=[[False]*(V+1) for _ in range(V+1)]
for _ in range(E):
    i,j,w = map(int,input().split())
    grid[i][j] = w

for k in range(1,V+1):
    for i in range(1,V+1):  
        for j in range(1,V+1):
            if grid[i][k] + grid[k][j] < grid[i][j]:
                grid[i][j] = grid[i][k] + grid[k][j]
                if i<=P or j<=P or k<=P:
                    red_pass[i][j] = True

def is_red(i,j):
    return red_pass[i][j] or i<=P or j<=P
sum_ = 0
count_ = 0
for _ in range(Q):
    i, j = map(int,input().split())
    sum_ += grid[i][j] if is_red(i,j) else 0
    count_ += 1 if is_red(i,j) else 0

print(count_)
print(sum_)