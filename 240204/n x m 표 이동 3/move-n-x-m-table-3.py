N, M = map(int, input().split())
K = int(input())
obstacles = [list(map(int,input().split())) for _ in range(K)]
blocked = [[[False,False] for _ in range(M+2)] for _ in range(N+2)]

for a,b,c,d in obstacles:
    [(a,b),(c,d)]=sorted([(a,b),(c,d)])
    dr = (c-a,d-b)
    if dr == (0,1):
        blocked[c+1][d+1][0] = True
    if dr == (1,0):
        blocked[c+1][d+1][1] = True
    

dp = [[0 for _ in range(M+2)] for _ in range(N+2)]
dp[1][1] = 1

for i in range(1, N+2):
    for j in range(1, M+2):
        if not blocked[i][j][0]:
            dp[i][j] = dp[i][j-1]
        if not blocked[i][j][1]:
            dp[i][j] += dp[i-1][j]

print(dp[-1][-1])