# 입력

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

#  본문

max_count = 0
for i in range(N-2):
    for j in range(N-2):
        count = 0

        for di in range(3):
            for dj in range(3):
                i2, j2 = i+di, j+dj
                count += grid[i2][j2]
        
        max_count = max(max_count, count)

print(max_count)