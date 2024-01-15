K, N = map(int, input().split())

answer = []
def dfs(seq):
    if len(seq)==N:
        print(' '.join(map(str,seq)))
        return
    
    for i in range(1, K+1):
        dfs([*seq, i])

dfs(answer)