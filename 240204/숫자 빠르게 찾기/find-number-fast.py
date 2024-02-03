N, M = map(int, input().split())
seq = list(map(int,input().split()))

def binary_search(num):
    left, right = 0, N-1
    while left <= right:
        mid = (left+right)//2
        if num<seq[mid]:
            right = mid-1
        elif num>seq[mid]:
            left = mid +1
        else:
            return mid+1
    return -1

for _ in range(M):
    print(binary_search(int(input())))