N = int(input())

lines = [list(map(int,input().split())) for _ in range(N)]
lines.sort()

dp = [0]*1001

for i in range(N):
    dp[i] = 1

    for j in range(i):
        s_i, _ = lines[i]
        _, e_j = lines[j]

        if e_j < s_i:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))