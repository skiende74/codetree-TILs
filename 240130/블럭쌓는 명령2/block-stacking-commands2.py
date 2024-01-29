N, K = map(int,input().split())
washes = [list(map(int,input().split())) for _ in range(K)]

check = [0]*(N+1)
for w_min, w_max in washes:
    for i in range(w_min, w_max+1):
        check[i] += 1

print(max(check))