from collections import Counter
N, M = map(int, input().split())
seq = list(map(int, input().split()))
c = Counter(seq)

for _ in range(M):
    print(c[int(input())])