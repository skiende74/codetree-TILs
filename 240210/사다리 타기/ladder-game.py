N, M = map(int,input().split())
lines = [list(map(int, input().split())) for _ in range(M)]
selected_lines = []

lines.sort(key=lambda x: (x[1],x[0]))

ans = 100000000
def dfs(i):
    global ans
    if i==M:
        if is_possible():
            ans = min(ans, len(selected_lines))
        return
    
    dfs(i+1)

    selected_lines.append(lines[i])
    dfs(i+1)
    selected_lines.pop()

def is_possible():
    nums1, nums2 = list(range(N)) , list(range(N))
    
    for a,b in selected_lines:
        nums1[a-1], nums1[a] = nums1[a], nums1[a-1]
    for a,b in lines:
        nums2[a-1], nums2[a] = nums2[a], nums2[a-1]
    
    return nums1 == nums2


dfs(0)
print(ans)