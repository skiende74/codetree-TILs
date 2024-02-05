N, Q = map(int, input().split())
NN = 1_000_000
nums = [0]*(NN+1)
for i in map(int,input().split()):
    nums[i] = 1
prefix_sum = [0]*(NN+1)

for i in range(1,NN+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

for _ in range(Q):
    a,b = map(int,input().split())
    print(prefix_sum[b] - prefix_sum[a-1])