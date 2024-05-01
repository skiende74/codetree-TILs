def union(i,j):
    r1,r2 = find(i), find(j)
    r = min(r1,r2)
    parent[r1] = r
    parent[r2] = r
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

N, M = map(int,input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    op, i, j = map(int,input().split())
    if op == 0:
        union(i,j)
    else:
        print(1 if find(i) == find(j) else 0 )