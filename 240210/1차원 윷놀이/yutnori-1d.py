N, M, K = map(int, input().split())
distances = list(map(int,input().split()))
pieces = [0]*K

ans = 0
def dfs(i):
    global ans
    if i == N:
        ans = max(ans, sum([1 for m in pieces if m>=M-1]))
        return

    for k in range(K):
        pieces[k] += distances[i]
        dfs(i+1)
        pieces[k] -= distances[i]

dfs(0)
print(ans)