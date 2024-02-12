N, S = map(int, input().split())
seq = [0]+list(map( int, input().split()))

prefix_sum = [0]*(N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1]+ seq[i]

i,j = 1,1
ans = 10**6
while i<=N and j<=N:
    total = prefix_sum[j] - prefix_sum[i-1]
    if total < S:
        j+=1
    else:
        ans = min(ans, j-i+1)
        i+=1
print(ans)