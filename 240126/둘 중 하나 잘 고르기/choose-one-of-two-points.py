N = int(input())
cards = [0]+[list(map(int, input().split())) for _ in range(2*N)]

dp = [[0]*(N+1) for _ in range(2*N+1)]

for i in range(1, 2*N+1):
    dp[i][0] = max(dp[i][0], dp[i-1][0] + cards[i][1])

for i in range(1, 2*N+1):
    a,b = cards[i]
    for j in range(1, min(i,N)+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a)
        dp[i][j] = max(dp[i][j], dp[i-1][j]+b)

#print(dp)
print(dp[2*N][N])