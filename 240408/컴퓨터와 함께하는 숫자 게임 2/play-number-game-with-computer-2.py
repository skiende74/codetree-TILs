N = int(input())
def binary(goal):
    left, right = 1, N
    
    count = 0
    while left<=right:
        mid = (left+right)//2
        count += 1
        if mid == goal: return count 
        if mid<goal: left = mid+1
        else: right = mid-1
    return count

numbers = list(range(*map(int,input().split())))
counted = list(map(binary, numbers))
print(min(counted),max(counted))