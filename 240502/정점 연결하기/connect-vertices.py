def union(i,j):
    r1, r2 = find(i), find(j)
    r = min(r1,r2)
    parent[r1]=r
    parent[r2]=r
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

N = int(input())
parent = [i for i in range(N+1)]
for _ in range(N-2):
    i, j = map(int,input().split())
    union(i,j)
print(*set(parent[1:]))