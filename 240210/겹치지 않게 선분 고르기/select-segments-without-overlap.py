N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]

points = []
for s, e in segments:
    points.append((s,+1))
    points.append((e,-1))

points.sort(key=lambda x: (x[0],-x[1]))

count = 0
ans = 0
for x,v in points:
    if count == 0 and v==1:
        ans += 1
    count += v

print(ans)