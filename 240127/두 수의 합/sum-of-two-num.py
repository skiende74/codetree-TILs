from itertools import combinations

N, K = map(int, input().split())
seq = list(map(int, input().split()))

result = 0
for a,b in combinations(seq, 2):
    if a+b == K:
        result +=1

print(result)