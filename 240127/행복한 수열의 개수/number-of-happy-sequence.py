# 입력
N, M = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(N)]

# 본문

happy_count = 0
# 열
for j in range(N):
    dup_count = 1
    for i in range(1, N):
        if grid[i][j] == grid[i-1][j]:
            dup_count += 1
    
    if dup_count >= M:
        happy_count += 1

# 행
for i in range(N):
    dup_count = 1
    for j in range(1, N):
        if grid[i][j] == grid[i][j-1]:
            dup_count += 1
    
    if dup_count >= M:
        happy_count += 1


print(happy_count)