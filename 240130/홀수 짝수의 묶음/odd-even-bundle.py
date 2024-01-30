N = int(input())
seq = list(map(int,input().split()))

even, odd = 0,0
for s in seq:
    if s%2==0:
        even += 1
    else:
        odd += 1

if even < odd:
    k = (odd-even+2)//3
    even += k
    odd -= 2*k

if even > odd:
    answer = odd*2+1
elif even == odd:
    answer = odd*2
print(answer)