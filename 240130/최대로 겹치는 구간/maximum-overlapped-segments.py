OFFSET = 100
MAX_R = 200

N = int(input())
segments = [list(map(int, input().split())) for _ in range(N)]

seq = [0]*(MAX_R+1)
for s,e in segments:
    for i in range(s,e):
        seq[i+OFFSET] += 1

print(max(seq))