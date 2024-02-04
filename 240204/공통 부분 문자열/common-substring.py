A, B = input(),input()
M, N = len(A), len(B)

dp=[[0]*(N+1) for _ in range(M+1)]
for i in range(1,M+1):
    for j in range(1,N+1):
        if A[i-1]==B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = dp[i-1][j-1]

print(dp[-1][-1])