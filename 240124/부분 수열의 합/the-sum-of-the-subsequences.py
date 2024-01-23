N, M = map(int, input().split())
seq = list(map(int, input().split()))

seq.sort()

answer = False
total = 0
def dfs(num, i):
    global answer
    if not i<N or num<0:
        return
    if num == seq[i]:
        answer = True
        return
       
    dfs(num-seq[i], i+1)
    dfs(num, i+1)

dfs(M, 0)

print('Yes' if answer else 'No')