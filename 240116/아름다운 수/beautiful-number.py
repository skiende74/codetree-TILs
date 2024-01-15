N = int(input())

answer = 0
def dfs(k):
    global answer
    if k == N:
        answer += 1
    
    if k>=N:
        return
    
    for i in range(1, 5):
        dfs(k+i)

dfs(0)
print(answer)