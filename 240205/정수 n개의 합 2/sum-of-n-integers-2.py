N, K = map(int, input().split())
seq = [0]+list(map(int, input().split()))

prefix_sum = [0]*(N+1)
total = sum(seq[:K])
max_total = total

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + seq[i]

for i in range(K, N):
    max_total = max(max_total, prefix_sum[i] - prefix_sum[i-K])

print(max_total)