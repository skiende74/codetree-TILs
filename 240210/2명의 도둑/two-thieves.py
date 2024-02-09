N, M, C = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

result = 0
def calc_value(arr):
    def calc_value_inner(i, w):
        global result
        if w > C or i == M:
            return 0

        res0 = sum(map(lambda x: x**2, selected_arr))    
        res1 = calc_value_inner(i+1, w)

        selected_arr.append(arr[i])
        res2 = calc_value_inner(i+1, w+arr[i])
        selected_arr.pop()
        return max(res1, res2, res0)

    selected_arr = []
    return calc_value_inner(0, 0)

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