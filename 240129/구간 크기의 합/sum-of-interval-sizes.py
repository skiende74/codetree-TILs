N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]

points = []
for s,e in segments:
    points.append((s,1))
    points.append((e,-1))
points.sort()

x_now, v_now = 0,0
x_start = 0
ans = 0
for x,v in points:
    x_now = x
    v_now += v

    if v_now == 0:
        ans += (x_now-x_start)
    
    if v_now == 1 and v==1:
        x_start = x

print(ans)