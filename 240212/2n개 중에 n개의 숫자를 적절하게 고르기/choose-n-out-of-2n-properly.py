N = int(input())
seq = [0] + list(map(int,input().split()))
selected = [False]*(2*N+1)

ans = 10**9
def dfs(i, j):
    global ans

    if j == N:
        ans = min(ans, calc())
        return
    if i == 2*N+1: return
    
    dfs(i+1, j)

    selected[i] = True
    dfs(i+1, j+1)
    selected[i] = False

def calc():
    total = 0
    for i in range(1,2*N+1):
        if selected[i]:
            total += seq[i]
        else:
            total -= seq[i]
    return abs(total)

dfs(1, 0)
print(ans)