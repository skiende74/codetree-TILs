N = int(input())
segments = [list(map(int, input().split())) for _ in range(N)]

points = []
for s,e in segments:
    points.append((s,1))
    points.append((e,-1))

points.sort()

n = 0
max_n = 0
for x,v in points:
    n += v
    max_n = max(max_n , n)
print(max_n)