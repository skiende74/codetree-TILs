N = int(input())
seq = list(map(int,input().split()))

val = 0
for i in range(N):
    val = max(seq[i], val+seq[i])
    ans = max(ans,val)
print(ans)