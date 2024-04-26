def dfs(i):
    if len(answers)==N:
        print(*answers)
    for j in range(N,0,-1):
        if not visited[j]:
            visited[j] = True
            answers.append(j)
            dfs(j)
            answers.pop()
            visited[j] = False

N = int(input())
visited= [False]*(N+1)
answers=[]
for j in range(N,0,-1):
    visited[j] = True
    answers.append(j)
    dfs(j)
    answers.pop()
    visited[j] = False