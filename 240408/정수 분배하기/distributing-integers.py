N, M = map(int, input().split())
seq = [int(input()) for _ in range(N)]

def f(k):
    return sum(map(lambda x: x//k, seq))

def custom_bound(f, goal):
    left, right = 0, min(seq)
    max_idx = left

    while left <= right:
        mid = (left+right)//2

        if f(mid) >= goal:
            left = mid + 1
            max_idx = max(max_idx, mid)
        else: right = mid-1
    return max_idx
print(custom_bound(f, M))