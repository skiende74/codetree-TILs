# 입력
N, M = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0]*(M+1) 
for i in range(1, M+1):
    for c in coins:
        if i-c>=0:
            dp[i] = max(dp[i], dp[i-c]+1)

if dp[M]==0:
    dp[M]=-1

print(dp[M])