from collections import defaultdict
def fibo(n):
    if memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = defaultdict(lambda: 0)
memo[1] = 1
memo[2] = 1

print(fibo(int(input())))