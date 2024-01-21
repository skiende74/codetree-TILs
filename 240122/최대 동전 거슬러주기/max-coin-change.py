# 입력
N, M = map(int, input().split())
coins = map(int, input().split())

seq = [1]+[0]*M

for i in range(1, M+1):
    for c in coins:
        if i-c>=0:
            seq[i] = max(seq[i], seq[i-c]+1)

print(seq[M])
print(seq)