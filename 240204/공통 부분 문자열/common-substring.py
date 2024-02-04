A, B = input(),input()
M, N = len(A), len(B)

dp=[[0]*(N+1) for _ in range(M+1)]

for i in range(M):
    for j in range(N):
        if A[i-1]==B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

print(dp[-1][-1])