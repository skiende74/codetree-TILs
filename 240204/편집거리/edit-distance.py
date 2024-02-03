A = input()
B = input()

M, N = len(A),len(B)

dp = [[0]*(N+1) for _ in range(M+1)]

for i in range(1,M+1):
    dp[i][0] = i
for j in range(1,N+1):
    dp[0][j] = j

for i in range(M):
    for j in range(N):
        if A[i]==B[j]:
            dp[i+1][j+1] = dp[i][j]
        else:
            dp[i+1][j+1] = min(dp[i][j+1],dp[i+1][j])+1


print(dp[-1][-1])