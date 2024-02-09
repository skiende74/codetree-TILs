import sys
sys.setrecursionlimit(10000)

N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]
segments_selected = []

ans = 0
def dfs(i):
    global ans
    if i==N:
        if is_possible():
            ans = max(ans, len(segments_selected))
        return

    dfs(i+1)
    segments_selected.append(segments[i])
    dfs(i+1)
    segments_selected.pop()

def is_possible():
    points = []
    for s,e in segments_selected:
        points.append((s,+1))
        points.append((e,-1))
    points.sort(key=lambda x: (x[0],-x[1]))

    count = 0
    for x,v in points:
        if count >= 1 and v==1:
            return False
        count += v
    return True

dfs(0)
print(ans)