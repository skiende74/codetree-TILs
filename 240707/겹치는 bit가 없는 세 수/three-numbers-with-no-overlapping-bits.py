N = int(input())
seq = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if seq[i] & seq[j] & seq[k] == 0:
                ans = max(ans, seq[i]|seq[j]|seq[k])
print(ans)