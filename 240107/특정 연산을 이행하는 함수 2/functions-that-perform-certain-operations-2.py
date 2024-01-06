from math import ceil, floor

a = list(map(float, input().split()))
maxVal = max(a)
minVal = min(a)
for i in range(3):
    if a[i] not in [minVal, maxVal]:
        mid = a[i]


print(f'{ceil(maxVal)} {floor(minVal)} {round(mid)}')