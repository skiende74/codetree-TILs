N = int(input())
now = 0

segments = []
for _ in range(N):
    l,direction = input().split()
    l = int(l)
    if direction == 'L':
        next = now-l
        segments.append([next, now])
    else:
        next = now+l
        segments.append([now, next])
    now = next

seq = [0]*(2001) #-1000~1000. OFFSET = 1000
OFFSET = 1000
for s,e in segments:
    for i in range(s,e):
        seq[i+OFFSET] += 1

ans = 0
for s in seq:
    if s>=2:
        ans += 1
print(ans)