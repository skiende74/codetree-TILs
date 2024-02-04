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

N,M = map(int, input().split())
seq = list(map(int,input().split()))
queries = list(map(int,input().split()))

for q in queries:
    ans = binary_lower(q)
    print(ans+1 if q == seq[ans] else -1)