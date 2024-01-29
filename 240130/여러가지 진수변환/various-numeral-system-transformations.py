N,B = map(int, input().split())

ans = ''
while N>0:
    N, k = divmod(N, B)
    ans = str(k) + ans
print(ans)