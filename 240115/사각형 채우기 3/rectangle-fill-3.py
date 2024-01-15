n = int(input())
memo = [0]*(1001)
memo[0]=1
memo[1]=2
for i in range(2,n+1):
    memo[i] = 2*memo[i-1]+3*memo[i-2]

print(memo[n])