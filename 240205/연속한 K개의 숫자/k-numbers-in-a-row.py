N,K,B = map(int, input().split())
nums = [0]*(N+1)
for _ in range(B):
    nums[int(input())] = 1

prefix_sum = [0]*(N+1)
for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]
    
ans = 1000_000_000
for i in range(K, N+1):
    ans = min(ans, prefix_sum[i] - prefix_sum[i-K])

print(ans)