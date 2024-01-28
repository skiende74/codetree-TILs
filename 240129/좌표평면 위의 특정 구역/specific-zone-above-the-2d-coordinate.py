N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]

result = 1000000000
for i in range(N):
    new_points = [*points[:i], *points[i+1:]]

    x0=min(new_points, key=lambda x: x[0])[0]
    x1=max(new_points, key=lambda x: x[0])[0]
    y0=min(new_points, key=lambda x: x[1])[1]
    y1=max(new_points, key=lambda x: x[1])[1]
    
    result = min(result, (x1-x0)*(y1-y0))
print(result)