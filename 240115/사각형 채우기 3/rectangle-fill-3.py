n = int(input())
memo = [0]*(1001)
memo[0]=1
memo[1]=2
for i in range(2,n+1):
    memo[i] = (2*memo[i-1]+4*memo[i-2])%1_000_000_007

print(memo[n])