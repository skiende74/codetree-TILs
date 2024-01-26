N, M = map(int, input().split())
seq = list(reversed([int(input()) for _ in range(N)]))

while True:
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            count += 1
        elif count>=M:
            for j in range(1, count+1):
                seq[i-j] = 0
            count = 1    
    if count>=M:
        for j in range(count):
            seq[-1-j]= 0

    if 0 not in seq:
        break
    
    new_seq = []
    for i in range(len(seq)):
        if seq[i] != 0:
            new_seq.append(seq[i])
    seq = new_seq    
    
print(len(seq))

for i in range(len(seq)):
    print(seq[-1-i])