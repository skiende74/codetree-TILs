n = int(input())
memo = [0]*11

memo[1]=1
memo[2]=2
memo[3]=memo[3-1]*memo[1] + memo[3-2]*memo[2]

for i in range(4,10):
    for j in range(1, i):
        memo[i] += memo[i-j]*memo[j]

print(memo[n])