N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]

points = []
for s,e in segments:
    points.append((s,1))
    points.append((e,-1))
points.sort()

v = 0
ans = []
x_start = 0
for x0,v0 in points:
    v += v0
    
    if v0 == -1:
        if v == 0:
            ans.append(x0-x_start)
    else:
        if v == 1:
            x_start = x0

print(max(ans))