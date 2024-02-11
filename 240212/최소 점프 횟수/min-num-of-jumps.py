N = int(input())
seq = [0] + list(map(int,input().split()))
INF = 10**9
ans = INF

count = 0
def dfs(i):
    global ans, count
    if i == N:
        ans = min(ans, count)
        return
    if i > N:
        return
    
    for di in range(1, seq[i] + 1):
        count += 1
        dfs(i+di)
        count -= 1
dfs(1)
print(ans)