N, K = map(int, input().split())
seq = list(map(int, input().split()))

total = sum(seq[:K])
max_total = total

for i in range(K, N):
    total += seq[i] - seq[i-K]
    max_total = max(max_total, total)

print(max_total)