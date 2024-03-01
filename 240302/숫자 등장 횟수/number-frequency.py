from collections import defaultdict
N, M = map(int,input().split())
seq = list(map(int,input().split()))
ks = list(map(int,input().split()))

my_dict = defaultdict(lambda:0)
for i, el in enumerate(seq):
    my_dict[el] += 1

result = []
for k in ks:
    result.append(my_dict[k])
print(' '.join(map(str, result)))