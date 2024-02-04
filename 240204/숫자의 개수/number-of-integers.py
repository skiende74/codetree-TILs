N, M = map(int, input().split())
seq = list(map(int, input().split()))

def binary_lower(target):
    left, right = 0, N-1
    min_idx = N
    
    while left <= right:
        mid = (left + right)//2
        if seq[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid-1
        else:
            left = mid + 1
    
    return min_idx
def binary_custom(target):
    left, right = 0, N-1
    max_idx = -1
    
    while left <= right:
        mid = (left + right)//2
        if seq[mid] <= target:
            max_idx = max(max_idx, mid)
            left = mid+1
        else:
            right = mid - 1
    
    return max_idx

for _ in range(M):
    target = int(input())
    print(binary_custom(target)-binary_lower(target)+1)