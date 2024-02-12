N = int(input())
selected = []

visited = [False]*(N+1)
def dfs_perm():
    if len(selected) == N:
        print(' '.join(map(str, selected)))

    for i in range(1, N+1):
        if visited[i]: continue
        visited[i] = True
        selected.append(i)
        dfs_perm()
        visited[i] = False
        selected.pop()

dfs_perm()