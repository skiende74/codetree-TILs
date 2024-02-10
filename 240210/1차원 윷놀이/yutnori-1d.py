N, M, K = map(int, input().split())
distances = list(map(int,input().split()))
selected = []

ans = 0
def dfs():
    global ans
    if len(selected) == N:
        move = [0]*K
        for i, dist in enumerate(distances):
            move[selected[i]] += dist
        ans = max(ans, sum([1 for m in move if m>=M-1]))
        return

    for i in range(K):
        selected.append(i)
        dfs()
        selected.pop()

dfs()
print(ans)