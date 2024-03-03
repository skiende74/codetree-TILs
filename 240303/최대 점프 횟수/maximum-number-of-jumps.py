N = int(input())
seq = list(map(int,input().split()))
dp = [0]*N

for i in range(1,N):
    for j in range(i):
        if seq[j] >= i-j:
            dp[i] = max(dp[i], dp[j]+1)

def answer():
    for i in range(1, N):
        if dp[i] == 0:
            return max(dp[:i])
    return max(dp)
print(answer())