N = int(input())
groups = [0]*N
for i in range(N):
    M, *group = map(int, input().split())
    for g in group: groups[i] |= 1<<g

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if groups[i] & groups[j] == 0: cnt += 1
print(cnt)