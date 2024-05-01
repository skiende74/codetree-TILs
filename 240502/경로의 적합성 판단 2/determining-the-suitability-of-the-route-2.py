def union(i,j):
    r1,r2 = find(i),find(j)
    parent[r1] = r2
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

ans = 1
N, M, K = map(int,input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    union(i,j)
queries = list(map(int,input().split()))
for i in range(K-1):
    if find(queries[i]) != find(queries[i+1]): ans = 0
print(ans)