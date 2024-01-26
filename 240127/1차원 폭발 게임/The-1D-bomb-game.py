N, M = map(int, input().split())
seq = [int(input()) for _ in range(N)]

while True:
    old = seq[0]
    count = 1
    for i in range(N):
        if old == seq[i]:
            count += 1
        elif count>=M:
            for j in range(1, count+1):
                seq[i-j] = 0
            count = 1
        old = seq[i]
    if count>=M:
        for j in range(1, count+1):
            seq[N-1-j] = 0

    new_seq = [-1]*N
    new_idx = 0
    is_zero_occur = False
    for i in range(N):
        if seq[i] != 0:
            new_seq[new_idx] = seq[i]
            new_idx += 1
        else:
            is_zero_occur = True
    seq = new_seq    
    if not is_zero_occur:
        break

for i in range(N):
    if seq[i] == -1:
        print(i)
        break
    print(seq[i])

for i in range(N):
    if seq[i] == -1:
        break
    print(seq[i])