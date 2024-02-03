N, M = map(int, input().split())

A = [['0']*(M) for _ in range(N) ]
k=1
for j in range(M):
    for i in range(N):
        A[i][j] = str(k)
        k+=1

for i in range(N):
    print(' '.join(A[i]))