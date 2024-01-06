from math import ceil, floor

a = list(map(float, input().split()))
maxVal = max(a)
minVal = min(a)

for i in range(3):
    num = a[i]
    if a[i]==maxVal:
        a[i] = str(ceil(a[i]))
    elif a[i]==minVal:
        a[i] = str(floor(a[i]))
    else:
        a[i] = str(round(a[i]))

print(' '.join(a))