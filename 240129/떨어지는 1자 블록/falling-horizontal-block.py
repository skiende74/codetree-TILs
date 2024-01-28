N, M, K = map(int,input().split()) # K,~~,K+M-1
grid = [list(map(int,input().split())) for _ in range(N)]

#
K -= 1
def simulate():
    for i in range(N-1):
        for j in range(K,K+M):
            if grid[i+1][j] == 1:
                return i    
    return N-1

i=simulate()
for j in range(K,K+M):
    grid[i][j] = 1
for i in range(N):
    print(' '.join(map(str, grid[i])))