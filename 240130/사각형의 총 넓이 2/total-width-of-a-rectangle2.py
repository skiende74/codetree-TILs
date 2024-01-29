N = int(input())
squares = [ list(map(int, input().split())) for _ in range(N)]

K_MAX = 100
OFFSET = K_MAX
grid = [[0]*(K_MAX*2+1) for _ in range(K_MAX*2 + 1)]
for x_min, y_min, x_max, y_max in squares:
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            grid[x+OFFSET][y+OFFSET] = 1

ans = 0
for x in range(2*K_MAX + 1):
    for y in range(2*K_MAX + 1):
        ans += grid[x][y]
print(ans)