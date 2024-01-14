readList = lambda: list(map(int, input().split()))
N, M, Q = readList()
grid = [readList() for _ in range(N)]



def blow(i, direction):
    seq = grid[i]
    if direction == 1:
        temp = seq[M-1]
        for j in range(M-1, 0, -1):
            seq[j] = seq[j-1]
        seq[0] = temp
    elif direction == -1:
        temp = seq[0]
        for j in range(M-1):
            seq[j] = seq[j+1]
        seq[M-1] = temp
    

    for di in [-1, 1]:
        i2 = i+di
        
        if 0<=i2<N and not visited[i2]:
            for j in range(M):
                if grid[i][j] == grid[i2][j]:
                    visited[i2] = True
                    blow(i2, direction*(-1))
                    break
        

# 본문

for _ in range(Q):
    i, direction = input().split()
    i = int(i)
    i -= 1
    visited = [False] * N
    visited[i] = True
    blow(int(i), 1 if direction == 'L' else -1)

for i in range(N):
    print(' '.join(map(str, grid[i])))