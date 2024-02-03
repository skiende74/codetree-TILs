K = int(input())
N = 5
visited = [[False]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    i, j = r-1, c-1
    visited[i][j] = True


def dfs(i1,j1,i2,j2, x):
    global answer
    if x in [25,26] and (i1,j1)==(i2,j2):
        answer += 1
        return
    dis, djs = [0,0,-1,1],[-1,1,0,0]
    for di, dj in zip(dis, djs):
        i1_, j1_ = i1+di, j1+dj
        if can_move(i1_,j1_):
            for di2, dj2 in zip(dis, djs):
                i2_, j2_ = i2+di2, j2+dj2
                if can_move(i2_, j2_):
                    visited[i1_][j1_] = True
                    visited[i2_][j2_] = True
                    dfs(i1_, j1_, i2_, j2_, x+2)
                    visited[i1_][j1_] = False
                    visited[i2_][j2_] = False 
         
def can_move(i,j):
    return 0<=i<N and 0<=j<N and not visited[i][j]

answer = 0
visited[0][0] = True
visited[4][4] = True
dfs(0,0,4,4,K+2)
print(answer)