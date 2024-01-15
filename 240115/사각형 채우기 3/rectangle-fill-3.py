n = int(input())
memo = [0]*(1001)
memo[0]=1
memo[1]=2
memo[2]=7
for i in range(3,n+1):
    #memo[i] = (2*memo[i-1]+3*memo[i-2]+2*memo[i-3])%1000000007
    memo[i] = (2*sum(memo[:i])+memo[i-2])%1_000_000_007

print(memo[n])