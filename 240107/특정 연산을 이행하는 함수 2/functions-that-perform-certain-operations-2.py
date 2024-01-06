from math import ceil, floor

a = list(map(float, input().split()))
maxVal = max(a)
minVal = min(a)


print(f'{ceil(maxVal)} {floor(minVal)} {round(a[2])}')