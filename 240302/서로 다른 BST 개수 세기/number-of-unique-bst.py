N = int(input())
UNUSED=-1
dp = [1,1]+[UNUSED]*(N-1)

def count(i):
    if dp[i] != UNUSED:
        return dp[i]
    
    if n<= 1: return 1
    
    result = 0
    for i in range(N):
        result += count(i)*count(N-i-1)
    dp[i] = result
    
    return dp[i]

print(count(N))