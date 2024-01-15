# 입력
n = int(input())

# 본문

def solve():
    if n==2:
        print(1)
        return
    memo = [0]*(n+1)
    memo[0] = 1
    memo[2] = 1
    memo[3] = 1

    for i in range(4,n+1):
        memo[i] = (memo[i-2]+memo[i-3])%10007

    print(memo[n])
solve()