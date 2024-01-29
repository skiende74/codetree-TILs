N = int(input())
segments = [list(map(int, input().split())) for _ in range(N)]

seq = [0]*(201)
for s,e in segments:
    for i in range(s,e):
        seq[i+100] += 1

print(max(seq))