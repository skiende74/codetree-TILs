n = int(input())
ans = ''

while n>0:
    n, k = divmod(n,2)
    ans = str(k) + ans
print(ans if ans else '0')