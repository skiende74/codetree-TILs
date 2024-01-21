N = int(input())
dp = [1]+[0]*(N)

nums = [1,2,5]
M = len(nums)

for i in range(1, N+1):
    for j in range(M):
        if i-nums[j] >= 0:
            dp[i] = (dp[i] + dp[i-nums[j]])%10007

print(dp[N])