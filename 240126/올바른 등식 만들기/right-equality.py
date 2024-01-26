N, M = map(int, input().split())
seq = [0] + list(map(int, input().split()))

dp = [[0]*20+[1]+[0]*20]+[ [0]*41 for _ in range(N)]

for i in range(1, N+1):
    num = seq[i]
    for j in range(-20, 20+1):
        if -20<=j-num<=20:
            dp[i][j+20] += dp[i-1][j-num+20]
        if -20<=j+num<=20:
            dp[i][j+20] += dp[i-1][j+num+20]
print(dp[N][M+20])