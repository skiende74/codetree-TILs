# 입력
N = int(input())
seq = [int(input()) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(2)]


# 본문
for s,e in commands:
    answer = []
    s,e = s-1, e-1
    for i in range(s,e+1):
        seq[i] = 0
    for a in seq:
        if a != 0:
            answer.append(a)
    seq = answer
    

print(len(answer))
print('\n'.join(map(str, answer)))