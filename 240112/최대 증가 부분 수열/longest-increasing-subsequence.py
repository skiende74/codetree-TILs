# 입력
N = int(input())
an = list(map(int, input().split()))

# 본문
dp = [1]*N
for i in range(N):
    for j in range(i):
        if an[j] < an[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))