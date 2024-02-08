K, N = map(int, input().split())

def dfs():
    if len(result) == N:
        print(' '.join(map(str, result)))
        return
    
    for k in range(1, K+1):
        result.append(k)
        dfs()
        result.pop()

result = []
dfs()