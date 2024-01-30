from heapq import heappush, heappop
from collections import defaultdict

N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]

points = []
for i,(y,s,e) in enumerate(segments):
    points.append((s,+1,i,y))
    points.append((e,-1,i, y))


lines = []
on_line = defaultdict(lambda:True)
ans = set()

def heappop_lines():
    while lines:
        y2, line_i2 = heappop(lines)
        if on_line[line_i2]:
            return (y2, line_i2)
    return (None, None)

points.sort(key=lambda x: (x[0]))
for x,v,line_i,y in points:
    # lines의 최하위선이 없거나, 최하위선보다 지금넣는게 작으면 ans.add(line_i)
    if v == 1:
        # y2, line_i2 = heappop_lines()

        # if y2 == None:
        #     ans.add(line_i)
        # elif y < y2:
        #     ans.add(line_i)
        #     heappush(lines, (y2, line_i2))
        heappush(lines,(y, line_i))
        y2, line_i2 = heappop_lines()
        if line_i2 == line_i:
            ans.add(line_i)
        heappush(lines, (y2, line_i2))
        
    # 만약 빼는 선이 lines의 최하위 선이고,
    # 그다음최하위선이 존재시 그 선을 add
    elif v == -1:
        y2, line_i2 = heappop_lines()
        if y2:
            if y == y2:
                y3, line_i3 = heappop_lines()
                if y3:
                    ans.add(line_i3)
                    heappush(lines, (y3,line_i3))
            heappush(lines, (y2, line_i2))
        on_line[line_i] = False

print(len(ans))