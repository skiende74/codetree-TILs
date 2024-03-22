N = int(input())

lines = [list(map(int,input().split())) for _ in range(N)]
lines.sort()

dp = [0]*1001

for s, e in lines:
    dp[e] = max(dp[e], dp[s-1] + 1)
print(max(dp))