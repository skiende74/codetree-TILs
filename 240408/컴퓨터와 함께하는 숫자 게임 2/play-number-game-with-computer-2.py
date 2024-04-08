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
a, b = map(int,input().split())
numbers = list(range(a,b+1))
counted = list(map(binary, numbers))
print(min(counted),max(counted))