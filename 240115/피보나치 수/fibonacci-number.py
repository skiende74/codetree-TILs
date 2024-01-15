def fibo(n):
    if memo[n] != 0:
        return memo[n]
    return fibo(n-1) + fibo(n-2)

memo = [0]*51
memo[1] = 1
memo[2] = 1

print(fibo(int(input())))