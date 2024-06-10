T = input()
P = input()
N = len(T)
M = len(P)

T = '#'+T
P = '#'+P



f = [0]*(M+1)
f[0] = -1
for i in range(1, M+1):
    j = f[i-1]
    while j>=0 and P[j+1] != P[i]: j = f[j]
    f[i] = j + 1

cnt = 0
j = 0
for i in range(1, N+1):
    while j>=0 and P[j+1] != T[i]: j = f[j]
    j += 1
    if j == M:
        cnt += 1
        j = f[j]

print(cnt)