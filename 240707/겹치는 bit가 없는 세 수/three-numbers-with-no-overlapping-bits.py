N = int(input())
seq = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if not(seq[i] & seq[j] or seq[j] & seq[k] or seq[k] & seq[i]):
                ans = max(ans, seq[i]|seq[j]|seq[k])
print(ans)