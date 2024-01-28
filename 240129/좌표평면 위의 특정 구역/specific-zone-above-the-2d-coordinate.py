N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]

result = 100000000000
x0 = (0,points[0][0])
y0 = (0,points[0][1])
x1,y1 = x0,y0
for i,(x,y) in enumerate(points):
    
    if x<=x0[1]:
        x0_2 = x0
        x0 = (i, x)
    if x>=x1[1]:
        x1_2 = x1
        x1 = (i, x)
    if y<=y0[1]:
        y0_2 = y0
        y0 = (i, y)
    if y>=y1[1]:
        y1_2 = y1
        y1 = (i, y)

for i in range(N):
    if i != x0[0]:
        xx0=x0[1]
    else:
        xx0=x0_2[1]

    if i != x1[0]:
        xx1=x1[1]
    else:
        xx1=x1_2[1]

    if i != y0[0]:
        yy0=y0[1]
    else:
        yy0=y0_2[1]

    if i != y1[0]:
        yy1=y1[1]
    else:
        yy1=y1_2[1]

    result = min(result, (xx1-xx0)*(yy1-yy0))
print(result)