# 입력
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 본문
def getSum(i,j):
    result = 0
    i0 = i
    while j<N-1:
        result += grid[i][j]
        i,j = i-1, j+1

    while i>0:
        result += grid[i][j]
        i,j = i-1, j-1
    
    while j>0:
        result += grid[i][j]
        i,j = i+1, j-1

    while i<i0:
        result += grid[i][j]
        i,j = i+1, j+1
    return result

result = 0
for i in range(2, N):
    for j in range(N-i, N-1):
        result = max(result, getSum(i,j))

print(result)