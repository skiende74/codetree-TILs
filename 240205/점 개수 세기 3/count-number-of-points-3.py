from collections import defaultdict

n, q = map(int, input().split())
points = list(map(int, input().split()))
mapper = {}
for i, point in enumerate(points):
    mapper[point] = i

for _ in range(q):
    a, b = map(int, input().split())
    print(mapper[b]-mapper[a]+1)