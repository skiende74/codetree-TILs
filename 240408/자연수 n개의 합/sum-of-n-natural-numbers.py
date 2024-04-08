s = int(input())

N = 10**10

f = lambda x: (x*(x+1))//2

def custom_bound(f, goal):
    left, right = 1, N

    max_idx = -1
    while left <= right:
        mid = (left + right)//2
        
        if f(mid) <= goal:
            max_idx = max(max_idx, mid)
            left = mid + 1
        else: right = mid-1
    return max_idx

print(custom_bound(f, s))