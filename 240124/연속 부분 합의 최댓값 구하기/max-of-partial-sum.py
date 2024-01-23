import sys

# 입력
N = int(input())
seq = list(map(int, input().split()))

# 초기화
INT_MIN = -sys.maxsize
dp = [INT_MIN]*N

dp[0] = seq[0]
# 본문
for i in range(1, N):
    dp[i] = max(dp[i-1]+seq[i], seq[i])

print(max(dp))