N = int(input())
seq = [0] + list(map(int,input().split()))
INF = 10**9
dp = [INF]*(N+1)
dp[1] = 0
for i in range(2, N+1):
    dp[i] = min([INF]+[dp[j]+1 if seq[j]+j >= i else INF for j in range(1, i)])
print(dp[-1])