n = int(input())
memo = [0]*11

memo[1]=1
memo[2]=2
memo[3]=memo[3-1] + memo[3-2] + 1

for i in range(4,10):
    memo[i] = sum(memo[1:i])+1

print(memo[n])