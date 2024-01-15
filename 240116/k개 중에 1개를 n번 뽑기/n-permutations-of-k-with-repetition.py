K, N = map(int, input().split())

answer = []
def dfs(k):
    if k==N:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(1, K+1):
        answer.append(i)
        dfs(k+1)
        answer.pop()

dfs(0)