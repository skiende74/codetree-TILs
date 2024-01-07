import sys
# 입력
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


# 개수세기
def count_block1(i,j):
    blocks = [*grid[i][j:j+2],*grid[i+1][j:j+2]]
    return sum(blocks) - min(blocks)
def count_block2(i,j):
    max_val = -1
    for ii in range(i, i+3):
        max_val = max(max_val, sum(grid[ii][j:j+3]))
    
    for jj in range(j, j+3):
        col = 0
        for ii in range(i, i+3):
            col += grid[ii][jj]
        max_val = max(max_val, col)

    return max_val

# 본문
result = 0
for i in range(N-1):
    for j in range(N-1):
        result = max(result, count_block1(i,j))

for i in range(N-2):
    for j in range(N-2):
        result = max(result, count_block2(i,j))

print(result)