N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

max_area2=0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            p1,p2,p3 = points[i],points[j],points[k]

            yy = p1[0] == p2[0] or p1[0] == p3[0] or p2[0] == p3[0]
            xx = p1[1] == p2[1] or p1[1] == p3[1] or p2[1] == p3[1]
            if xx and yy:
                area2 = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]-(p1[1]*p2[0]+p2[1]*p3[0]+p3[1]*p1[0])
                max_area2 = max(max_area2, area2)
print(max_area2)