N, M, C = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

def calc_value(arr):
    arr.sort(key=lambda x: -x)
    w = 0
    for i, val in enumerate(arr):
        w += val
        if w > C:
            arr = arr[:i]
        
    return sum(map(lambda x: x**2, arr))

values = [0]*N
for i in range(N):
    for j in range(N-M+1):
        values[i] = max(values[i], calc_value(grid[i][j:j+M]))

ans = 0
for i1 in range(N):
    for i2 in range(i1+1, N):
        ans = max(ans, values[i1] + values[i2])

for i in range(N):
    for j1 in range(N):
        for j2 in range(j1+M, N-M+1):
            ans = max(ans, calc_value(grid[i][j1:j1+M]) + calc_value(grid[i][j2:j2+M]))

print(ans)