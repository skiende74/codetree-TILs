# 입력
N = int(input())
grid = [ list(map(int, input().split())) for _ in range(N)]

max_total = 0
for i in range(1,N-1):
    for j in range(1, N-1):
        total = 0

        for di in range(-1,2):
            for dj in range(-1,2):
                i2,j2 = i+di,j+dj
                total += grid[i2][j2]
        
        max_total = max(max_total, total)

print(max_total)