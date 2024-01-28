N, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

r, c = r-1, c-1

result = [grid[r][c]]
def do():
    i,j = r, c
    while True:

        dis, djs = [-1,1,0,0],[0,0,-1,1]

        for di, dj in zip(dis,djs):
            i2,j2 = i+di, j+dj

            if 0<=i<N and 0<=j<N and grid[i2][j2] > grid[i][j]:
                result.append(grid[i2][j2])
                i,j = i2,j2
                break
        else:
            return
do()
print(' '.join(map(str, result)))