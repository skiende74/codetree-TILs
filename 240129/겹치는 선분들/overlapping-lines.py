N, K = map(int,input().split())
segments = [input().split() for _ in range(N)]

x = 0
points = []
for l,direction in segments:
    l = int(l)
    if direction == 'L':
        points.append((x,-1))
        x -= l
        points.append((x,+1))
    else:
        points.append((x,+1))
        x += l
        points.append((x,-1))

points.sort()
x_old, v_total = int(points[0][0]), points[0][1]
ans = 0
for x,v in points[1:]:
    if v_total >= K:
        ans += (x-x_old)
    v_total += v
    x_old = x

print(ans)