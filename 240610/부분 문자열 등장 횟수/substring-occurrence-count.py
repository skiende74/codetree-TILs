T = input()
P = input()
N = len(T)
M = len(P)

T = '#'+T
P = '#'+P



f = [0]*(M+1)
f[0] = -1
j = -1
for i in range(1,M+1):
    while j>=0 and P[i] != P[j+1]: j = f[j]
    j += 1
    f[i] = j

cnt = 0
for i in range(1, N+1):
    while j>=0 and T[i] != P[j+1]: j = f[j]
    j += 1
    if j == M:
        cnt += 1
        j = f[j]

print(cnt)