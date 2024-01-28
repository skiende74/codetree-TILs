def gcd(i,j):
    if j==0:
        return i
    return gcd(j,i%j)

i,j = map(int, input().split())
print(gcd(i,j))