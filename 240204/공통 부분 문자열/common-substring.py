A, B = input(),input()
M, N = len(A), len(B)

dp=[[0 for _ in range(N+1)] for _ in range(M+1)]
for i in range(1,M+1):
    for j in range(1,N+1):
        if A[i-1]==B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = 0

max_dp = 0
for i in range(1,M+1):
    for j in range(1,N+1):
        if dp[i][j]>max_dp:
            max_dp=dp[i][j]
print(max_dp)