N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]

points = []
for seg in segments:
    s,e = seg
    points.append((s,1))
    points.append((e,-1))

points.sort()

total = 0
num_of_region = 0
for x,v in points:
    if v==1:
        if total == 0:
            num_of_region += 1
    total += v

print(num_of_region)