N = int(input())
ans = []
selected = []
visited = [False]*(N+1)

def dfs_perm():
    if len(selected) == N:
        print(' '.join(map(str, selected)))
        return

    for i in range(N, 0, -1):
        if visited[i]: continue
        visited[i] = True
        selected.append(i)
        dfs_perm()
        visited[i] = False
        selected.pop()

dfs_perm()