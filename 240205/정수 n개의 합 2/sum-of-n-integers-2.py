N, K = map(int, input().split())
seq = list(map(int, input().split()))

total = sum(seq[:5])
max_total = total

for i in range(5, N):
    total += seq[i] - seq[i-5]
    max_total = max(max_total, total)

print(max_total)