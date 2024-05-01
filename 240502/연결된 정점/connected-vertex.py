from collections import Counter
N, Q = map(int,input().split())
parent = [i for i in range(N+1)]
def union(i,j):
    r1,r2 = find(i), find(j)
    parent[r1] = r2
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

search = []
for _ in range(Q):
    query = input().split()
    if query[0] == 'x':
        i, j = map(int,query[1:])
        union(i,j)
    else:
        search.append(int(query[1]))
for i in range(1,N+1):
    find(i)
counter = Counter(parent)
for s in search:
    print(counter[parent[s]])