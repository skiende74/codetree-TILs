N = int(input())

def dfs(i):
    if len(answers)==N:
        print(*answers)
    for j in range(1,N+1):
        if not visited[j]:
            visited[j] = True
            answers.append(j)
            dfs(j)
            answers.pop()
            visited[j] = False

for i in range(1,N+1):
    visited = [False]*(N+1)
    visited[i] = True
    answers = [i]
    dfs(i)