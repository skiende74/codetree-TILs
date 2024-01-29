N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 본문

max_total = 0
# 1
for i in range(N-1):
    for j in range(M-1):

        total = 0
        for di in range(2):
            for dj in range(2):
                i2,j2 = i+di, j+dj
                total += grid[i2][j2]
        
        for di,dj in zip([0,0,1,1], [0,1,0,1]):
            i2,j2 = i+di, j+dj
            max_total = max(max_total, total-grid[i2][j2])
    
# 2-1. 가로
for i in range(N):
    for j in range(M-2):
        total = sum(grid[i][j:j+3])
        max_total = max(max_total, total)

# 2-2. 세로
for i in range(N-2):
    for j in range(M):
        total = 0
        for di in range(3):
            i2,j2 = i+di, j
            total += grid[i2][j2]
        max_total = max(max_total, total)

print(max_total)