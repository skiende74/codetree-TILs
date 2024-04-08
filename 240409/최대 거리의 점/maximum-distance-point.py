N, M = map(int, input().split())
seq = [int(input()) for _ in range(N)]
seq.sort()

# 최소거리 -> 물건갯수. 감소
def f(x):
    count = 1
    s_old = seq[0]
    for s in seq[1:]:
        if s-s_old  >= x:
            s_old = s
            count += 1
    return count

def custom_bound(goal):
    
    left, right = 1, seq[-1]-seq[0]
    max_idx = 1

    while left<=right:
        mid = (left+right)//2

        if f(mid) >= goal:
            left = mid+1
            max_idx = max(max_idx, mid)
        else: right = mid-1
    return max_idx

print(custom_bound(M))