a = input()
p = input()

M, N = len(a), len(p)

dp = [[False]*(N+1) for _ in range(M+1)]

#
for i in range(1, M+1):
    dp[i][0] = True
for j in range(1, N+1):
    dp[0][j] = False # .*.* 에외잖아?
dp[0][0] = True

for i in range(1, M+1):
    for j in range(1, N+1):
        if p[j-1] == '.':
            dp[i][j] = dp[i-1][j-1]
        elif p[j-1] == '*':
            dp[i][j] = any([dp[i][j-2], dp[i][j-1]])
            dp[i][j] = dp[i][j] or (dp[i-1][j] and (a[i-1]==p[j-2] or p[j-2]=='.'))
        else:
            dp[i][j] = dp[i-1][j-1] and a[i-1] == p[j-1]

print('true' if dp[-1][-1] else 'false')