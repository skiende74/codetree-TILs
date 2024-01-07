# 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 본문
def solve():
    if M == 1:
        print(2*N)
        return
    happy_count = 0
    for i in range(N):
        repeat_count = 1
        old = grid[i][0]
        for j in range(1, N):
            if grid[i][j] == old:
                repeat_count += 1
            else:
                old = grid[i][j]
                repeat_count = 1
            
            if repeat_count == M:
                happy_count += 1
                break

    for j in range(N):
        repeat_count = 1
        old = grid[0][j]
        for i in range(1, N):
            if grid[i][j] == old:
                repeat_count += 1
            else:
                old = grid[i][j]
                repeat_count = 1
            
            if repeat_count == M:
                happy_count += 1
                break

    print(happy_count)
solve()