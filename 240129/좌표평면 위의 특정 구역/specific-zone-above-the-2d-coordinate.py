from copy import copy

N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]

result = 100000000000


def min2(x, key, sel):
    x = copy(x)
    
    min_x = min(x, key=key)
    min_idx = x.index(min_x)
    x.pop(min_idx)
    min_x2 = min(x, key=key)
    min_idx2 = x.index(min_x2)
    if min_idx<=min_idx2:
        min_idx2 += 1
    
    return [[min_x[sel],min_idx],[min_x2[sel], min_idx2]]
[[x0, x0_idx],[x0_2,_]] = min2(points, lambda x:x[0], 0)
[[x1, x1_idx],[x1_2,_]] = min2(points, lambda x:-x[0], 0)
[[y0, y0_idx],[y0_2,_]] = min2(points, lambda x:x[1], 1)
[[y1, y1_idx],[y1_2,_]] = min2(points, lambda x:-x[1], 1)

for i in range(N):
    if i != x0_idx:
        xx0 = x0
    else:
        xx0=x0_2

    if i != x1_idx:
        xx1=x1
    else:
        xx1=x1_2

    if i != y0_idx:
        yy0=y0
    else:
        yy0=y0_2

    if i != y1_idx:
        yy1=y1
    else:
        yy1=y1_2

    result = min(result, (xx1-xx0)*(yy1-yy0))
# print(x0,x0_2,y0,y0_2)
# print(x1,x1_2,y1,y1_2)
# print(x0_idx, y0_idx, x1_idx, y1_idx)
print(result)