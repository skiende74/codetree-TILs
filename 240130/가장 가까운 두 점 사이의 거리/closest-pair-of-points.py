import sys

N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]

min_dist = sys.maxsize
for i in range(N):
    for j in range(i+1, N):
        p1, p2 = points[i], points[j]

        dist = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        min_dist = min(min_dist, dist)
print(min_dist)