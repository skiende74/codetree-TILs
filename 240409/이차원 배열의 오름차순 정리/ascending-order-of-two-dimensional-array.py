from math import ceil

def num2k(num): 
    result = 0

    for k in range(1,n+1):
        result += min(n,num//k)
    return result

def lower_bound(f, goal):
    left, right = 1, n*n
    min_idx = n*n

    while left <= right:
        mid = (left+right)//2
        if f(mid) >= goal:
            right = mid -1
            min_idx = min(min_idx, mid)
        else: left = mid + 1
    return min_idx
n = int(input())
print(lower_bound(num2k, int(input())))