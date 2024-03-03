import sys
INT_MIN = -sys.maxsize

N = int(input())
seq = list(map(int,input().split()))
dp = [INT_MIN]*N
dp[0] = 0
for i in range(1,N):
    for j in range(i):
        if seq[j] >= i-j and dp[j] != INT_MIN:
            dp[i] = max(dp[i], dp[j]+1)

print(dp[-1])