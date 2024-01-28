M = 200000
N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]

points = []
seq = [0]*(M+1)
for seg in segments:
    i, j = seg
    seq[i] += 1
    seq[j] -= 1

total = 0
max_total = 0
for i in range(1,M+1):
    total += seq[i]
    max_total = max(max_total, total)

print(max_total)