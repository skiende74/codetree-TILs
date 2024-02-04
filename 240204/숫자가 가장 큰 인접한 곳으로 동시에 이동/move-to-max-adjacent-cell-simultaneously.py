from copy import deepcopy
N, M, t = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
balls = [list(map(int,input().split())) for _ in range(M)]
count = [[0]*N for _ in range(N)]
for r,c in balls:
    i,j = r-1,c-1
    count[i][j] = 1

rounds = 0
while rounds<t:
    new_count = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if count[i][j] > 2:
                new_count[i][j] = 0
            elif count[i][j] == 1:
                dis, djs = [0,0,-1,1],[-1,1,0,0]
                priority = -1
                for di, dj in zip(dis,djs):
                    i2,j2 = i+di, j+dj
                    if 0<=i2<N and 0<=j2<N and grid[i2][j2] > priority:
                        priority = grid[i2][j2]
                        i_next, j_next = i2,j2
                new_count[i_next][j_next] += 1
    count = deepcopy(new_count)
    rounds += 1
ans = 0
for i in range(N):
    for j in range(N):
        ans += count[i][j]
print(ans)