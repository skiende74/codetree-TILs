A,B = input(),input()
M,N = len(A),len(B)

dp = [['' for _ in range(N+1)] for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + A[i-1]
        elif dp[i][j-1]>dp[i-1][j]:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])