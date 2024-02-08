# 입력
N = int(input())

# dfs
def dfs():
    global ans, result
    if len(result) == N:
        ans += 1
        return
    if len(result) > N:
        return
    
    for i in range(1,5):
        result += [i]*i
        dfs()
        result = result[:-i]

ans = 0
result = []
dfs()
print(ans)