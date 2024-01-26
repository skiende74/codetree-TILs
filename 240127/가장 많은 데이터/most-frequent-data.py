from collections import defaultdict
N = int(input())

counter = defaultdict(lambda:0)
for _ in range(N):
    counter[input()] += 1

print(max(counter.values()))