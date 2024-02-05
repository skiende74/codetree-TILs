N, K = map(int, input().split())
seq = [0] + list(map(int,input().split()))
prefix_sum = [0]*(N+1)

for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + seq[i]

ans=0
for i in range(N+1):
    for j in range(i+1, N+1):
        if prefix_sum[j] - prefix_sum[i] == K:
            ans+=1
print(ans)