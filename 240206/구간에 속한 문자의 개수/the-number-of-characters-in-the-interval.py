N,M,K = map(int,input().split())
grid = [['0']*(M+1)] + [ ['0'] + list(input()) for _ in range(N)]
prefix_sum = [[[0,0,0] for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if grid[i][j] == 'a':
            a = [1,0,0]
        elif grid[i][j] == 'b':
            a = [0,1,0]
        else:
            a = [0,0,1]

        for k in range(3):
            prefix_sum[i][j][k] = prefix_sum[i][j-1][k] + prefix_sum[i-1][j][k] - \
            prefix_sum[i-1][j-1][k] + a[k]

for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    ans = [0,0,0]
    for k in range(3):
        ans[k] = prefix_sum[r2][c2][k] - prefix_sum[r2][c1-1][k] - prefix_sum[r1-1][c2][k] + \
        prefix_sum[r1-1][c1-1][k]
    print(' '.join(map(str, ans)))