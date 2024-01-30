N, M = map(int, input().split())
seq = list(map(int,input().split()))

prev = -1000
count = 0
for i, s in enumerate(seq):
    if s==1 and i>prev+M:
        prev = i+M
        count += 1
print(count)