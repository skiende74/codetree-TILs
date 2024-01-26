from collections import Counter
from itertools import combinations
N, K = map(int, input().split())
seq = list(map(int, input().split()))

result = 0
for ((a,a_c),(b,b_c)) in combinations(Counter(seq).items(), 2):
    if a+b == K:
        result +=a+c*b_c

print(result)