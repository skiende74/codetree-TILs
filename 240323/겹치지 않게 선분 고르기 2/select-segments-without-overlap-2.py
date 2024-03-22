N = int(input())

lines = [list(map(int,input().split())) for _ in range(N)]
lines.sort(key=lambda x: (x[1]))

dp = [0]*1001

for s, e in lines:
    dp[e] = max(dp[e], dp[s-1] + 1)
print(max(dp))