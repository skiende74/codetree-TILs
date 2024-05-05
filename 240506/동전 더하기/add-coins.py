N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]

count = 0
for c in coins[::-1]:
    dc,K = divmod(K,c)
    count += dc
print(count)