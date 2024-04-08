def binary_lower(target):
    left, right = 0, N-1
    min_idx = N

    while left<=right:
        mid = (left+right)//2

        if seq[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return min_idx

from bisect import bisect_left

N,M = map(int, input().split())
seq = list(map(int,input().split()))
queries = list(map(int,input().split()))

for q in queries:
    ans = binary_lower(q)
    ans = bisect_left(seq,q)
    print(ans+1 if ans < N and q == seq[ans] else -1)