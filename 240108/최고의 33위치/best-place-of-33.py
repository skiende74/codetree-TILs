# 입력
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]


# coin
def coin(i,j):
    result = 0
    for ii in range(i,i+3):
        for jj in range(j, j+3):
            result += grid[ii][jj]
    return result

# 본문
coin_max = 0
for i in range(N-2):
    for j in range(N-2):
        coin_max = max(coin_max, coin(i,j))

print(coin_max)