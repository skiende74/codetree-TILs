N = int(input())

ans = ''
result = []
def dfs():
    global ans
    if len(ans) == N:
        result.append(ans)
        return

    for i in range(4,7):
        ans += str(i)

        n = len(ans)//2
        is_possible = True
        for k in range(1, n + 1):
            if ans[-2*k:-k] == ans[-k:]:
                is_possible = False
        if is_possible:
            dfs()
        ans = ans[:-1]
dfs()
print(result[0])