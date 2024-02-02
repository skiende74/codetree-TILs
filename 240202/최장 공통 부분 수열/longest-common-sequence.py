A, B = input(), input()
N, M = len(A), len(B)
import sys

dp = [[0]*(M+1) for _ in range(N+1)]
dp[1][1] = 1 if A[0] == B[0] else 0

for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])