def union(i,j):
    r1,r2 = find(i),find(j)
    parent[r1] = r2
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]
N, M = map(int,input().split())
parent = [i for i in range(N+1)]
answer = 'happy'
for num in range(1,M+1):
    i, j = map(int,input().split())
    if find(i)==find(j):
        answer = num
        break
    union(i,j)
print(answer)