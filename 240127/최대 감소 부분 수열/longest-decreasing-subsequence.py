N = int(input())
seq = list(map(int, input().split()))

dp = [1]*N
for i in range(N):
    for j in range(i):
        if seq[j]>seq[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1

print(max(dp))