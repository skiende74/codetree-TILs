N = int(input())

lines = [list(map(int,input().split())) for _ in range(N)]
lines.sort(key=lambda x: (x[1],x[0]))

dp = [0]*1001

for i in range(N):
    dp[i] = 1

    for j in range(i):
        s_i, _ = lines[i]
        _, e_j = lines[j]

        dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))