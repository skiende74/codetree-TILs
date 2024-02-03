A = input()
B = input()

M, N = len(A),len(B)

dp = [[0]*(N+1) for _ in range(M+1)]
for i in range(M):
    for j in range(N):
        if A[i]==B[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

print(dp[-1][-1])