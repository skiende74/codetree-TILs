A,B = input(),input()
M,N = len(A),len(B)

dp = [['' for _ in range(N)] for _ in range(M)]

for i in range(M):
    for j in range(N):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + A[i]
        elif dp[i][j-1]>dp[i-1][j]:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])