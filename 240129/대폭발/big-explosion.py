from collections import defaultdict

N,M,r,c = map(int, input().split())

count = defaultdict(lambda:0)
visited = [[[False]*N for _ in range(N)]]
def dfs(i,j, t):
    if t==M:
        return

    dis, djs = [-1,1,0,0,0],[0,0,-1,1,0]
    for di, dj in zip(dis,djs):
        i2,j2 = i+(2**t)*di, j+(2**t)*dj
        if 0<=i2<N and 0<=j2<N and not visited[i2][j2]:
            visited[t+1][i2][j2] = True
            count[t+1] += 1
            dfs(i2,j2, t+1)
    
r,c = r-1,c-1
dfs(r,c,0)
print(count[m])