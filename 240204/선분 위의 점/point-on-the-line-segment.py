readlist = lambda: list(map(int,input().split()))
N, M = readlist()
points = readlist()
lines = [ readlist() for _ in range(M)]

def binary_lower(target):
    left, right = 0, N-1
    min_idx = N

    while left<=right:
        mid = (left+right)//2

        if points[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid-1
        else:
            left = mid+1
    return min_idx

for l_min,l_max in lines:
    ans = binary_lower(l_max+1)-binary_lower(l_min)
    print(ans)