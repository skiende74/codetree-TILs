N, K = map(int, input().split())
seq = list(map(int, input().split()))

prefix_sum = [0]*(N+1)
total = sum(seq[:K])
max_total = total

for i in range(N):
    prefix_sum[i] = prefix_sum[i-1] + seq[i-1]

for i in range(K, N):
    max_total = max(max_total, prefix_sum[i] - prefix_sum[i-K])

print(max_total)