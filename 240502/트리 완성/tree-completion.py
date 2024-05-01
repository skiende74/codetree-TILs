def union(i,j):
    r1,r2 = find(i),find(j)
    parent[r1] = r2
def find(i):
    if parent[i]==i: return i
    parent[i] = find(parent[i])
    return parent[i]

N, M = map(int,input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    union(i,j)
for i in range(1,N+1): find(i)
print(len(set(parent[1:]))-1)