def count(k):
    return k-k//3-k//5+k//15

def lower_bound(f, goal):
    left, right = 1, 10**15
    min_idx = 10**15

    while left<=right:
        mid = (left+right)//2
        if f(mid) >= goal:
            right = mid -1
            min_idx = min(min_idx, mid)
        else: left = mid + 1

    return min_idx

print(lower_bound(count, int(input())))