import sys
N = int(input())
seq = list(map(int, input().split()))

MIN = -sys.maxsize
dp = [0] +[MIN]*(N-1)

for i in range(1, N):
    for j in range(i):
        if seq[j]>=i-j and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(max(dp))