N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]

seq = [0]*(101)
for s,e in segments:
    for i in range(s,e+1):
        seq[i]+=1
print(max(seq))