N, Q = map(int, input().split())
rocks = [0] + [int(input()) for _ in range(N)]
prefix_sum = [[0,0,0] for _ in range(N+1)]
for i in range(1,N+1):
    rock = [0,0,0]
    rock[rocks[i]-1] = 1
    for k in range(3):
        prefix_sum[i][k] = prefix_sum[i-1][k] + rock[k]

for _ in range(Q):
    a,b = map(int,input().split())
    ans = []
    for k in range(3):
        ans.append(prefix_sum[b][k] - prefix_sum[a-1][k])
    print(' '.join(map(str, ans)))